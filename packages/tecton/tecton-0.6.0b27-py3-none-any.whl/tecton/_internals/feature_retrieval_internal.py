from datetime import datetime
from typing import Optional
from typing import Union

import pandas as pd
import pendulum
import pyspark
from pyspark.sql import functions

from tecton._internals import data_frame_helper
from tecton._internals import errors as internal_errors
from tecton._internals.feature_views import aggregations
from tecton._internals.utils import is_live_workspace
from tecton.interactive.data_frame import TectonDataFrame
from tecton.tecton_context import TectonContext
from tecton_core import conf
from tecton_core import errors as core_errors
from tecton_core.errors import TectonValidationError
from tecton_core.feature_definition_wrapper import FeatureDefinitionWrapper as FeatureDefinition
from tecton_core.logger import get_logger
from tecton_core.query.builder import build_get_features
from tecton_core.query.builder import build_get_full_agg_features
from tecton_core.query.nodes import AddEffectiveTimestampNode
from tecton_core.query.nodes import ConvertEpochToTimestampNode
from tecton_core.query.nodes import FeatureTimeFilterNode
from tecton_core.query.nodes import JoinNode
from tecton_core.query.nodes import RenameColsNode
from tecton_core.query.nodes import SelectDistinctNode
from tecton_core.query.nodes import UserSpecifiedDataNode
from tecton_core.query_consts import ANCHOR_TIME
from tecton_core.query_consts import EFFECTIVE_TIMESTAMP
from tecton_proto.data.feature_view_pb2 import MaterializationTimeRangePolicy
from tecton_spark.materialization_params import MaterializationParams
from tecton_spark.query_utils import add_effective_timestamp
from tecton_spark.schema_spark_utils import schema_to_spark

logger = get_logger("FeatureRetrieval")


def get_features(
    fd: FeatureDefinition,
    entities: Optional[Union[pyspark.sql.dataframe.DataFrame, pd.DataFrame, TectonDataFrame]] = None,
    start_time: Optional[Union[pendulum.DateTime, datetime]] = None,
    end_time: Optional[Union[pendulum.DateTime, datetime]] = None,
    from_source: bool = False,
) -> TectonDataFrame:
    if fd.is_on_demand:
        raise internal_errors.FV_NOT_SUPPORTED_GET_HISTORICAL_FEATURES

    if from_source and fd.is_feature_table:
        raise TectonValidationError("FeatureTables are not compatible with from_source=True")

    if from_source and fd.is_incremental_backfill:
        raise core_errors.FV_BFC_SINGLE_FROM_SOURCE

    if not from_source and not is_live_workspace(fd.workspace):
        raise internal_errors.FD_GET_MATERIALIZED_FEATURES_FROM_DEVELOPMENT_WORKSPACE(fd.name, fd.workspace)

    if not from_source and not fd.writes_to_offline_store:
        raise internal_errors.FD_GET_FEATURES_MATERIALIZATION_DISABLED(fd.name)

    if start_time is not None and isinstance(start_time, datetime):
        start_time = pendulum.instance(start_time)
    if end_time is not None and isinstance(end_time, datetime):
        end_time = pendulum.instance(end_time)

    if start_time is not None and fd.feature_start_timestamp is not None and start_time < fd.feature_start_timestamp:
        logger.warning(
            f'The provided start_time ({start_time}) is before "{fd.name}"\'s feature_start_time ({fd.feature_start_timestamp}). No feature values will be returned before the feature_start_time.'
        )
        start_time = fd.feature_start_timestamp

    if fd.is_temporal_aggregate or fd.is_temporal:
        params = MaterializationParams.from_feature_definition(fd)
        assert params is not None, "Materialization params cannot be None"
        # Feature views where materialization is not enabled may not have a feature_start_time.
        _start = start_time or fd.feature_start_timestamp or pendulum.datetime(1970, 1, 1)
        # we need to add 1 to most_recent_anchor since we filter end_time exclusively
        _end = end_time or (params.most_recent_anchor(pendulum.now("UTC")) + pendulum.duration(microseconds=1))
    else:
        _start = start_time or pendulum.datetime(1970, 1, 1)
        _end = end_time or pendulum.now("UTC")

    time_range = pendulum.Period(_start, _end)

    tc = TectonContext.get_instance()
    spark = tc._spark

    if conf.get_bool("QUERYTREE_ENABLED"):

        # TODO(felix): Move this logic to `builder.py` once it does not rely on Spark-specific time util functions.
        if fd.is_temporal or fd.is_feature_table:
            qt = build_get_features(fd, from_source=from_source, feature_data_time_limits=time_range)
            qt = RenameColsNode(qt, drop=[ANCHOR_TIME]).as_ref()
            qt = AddEffectiveTimestampNode(
                qt,
                timestamp_field=fd.timestamp_key,
                effective_timestamp_name=EFFECTIVE_TIMESTAMP,
                batch_schedule_seconds=int(fd.batch_materialization_schedule.total_seconds()),
                data_delay_seconds=fd.online_store_data_delay_seconds,
                is_stream=fd.is_stream,
                is_temporal_aggregate=False,
            ).as_ref()
        else:
            raw_data_time_limits = aggregations._get_time_limits(
                fd=fd,
                spine_df=None,
                spine_time_limits=time_range,
            )
            # TODO(brian): rename feature_data_time_limits during cleanup
            # TODO(brian): refactor to share more with run api full aggregation
            qt = build_get_full_agg_features(
                fd,
                from_source=from_source,
                feature_data_time_limits=raw_data_time_limits,
            )

            # The `FullAggNode` returned by `build_get_full_agg_features` converts timestamps to epochs. We convert back
            # from epochs to timestamps so that we can add an effective timestamp column.
            qt = ConvertEpochToTimestampNode(qt, {ANCHOR_TIME: fd.get_feature_store_format_version}).as_ref()

            # TODO(alvin): After full aggregation, the _anchor_time definition changes from start -> end.
            # This is confusing. We should use different name other than _anchor_time.
            qt = RenameColsNode(qt, mapping={ANCHOR_TIME: fd.trailing_time_window_aggregation.time_key}).as_ref()
            qt = AddEffectiveTimestampNode(
                qt,
                timestamp_field=fd.trailing_time_window_aggregation.time_key,
                effective_timestamp_name=EFFECTIVE_TIMESTAMP,
                batch_schedule_seconds=int(fd.batch_materialization_schedule.total_seconds()),
                data_delay_seconds=fd.online_store_data_delay_seconds,
                is_stream=fd.is_stream,
                is_temporal_aggregate=True,
            ).as_ref()

        # Validate that entities only contains Join Key Columns.
        if entities is not None:
            if not isinstance(entities, TectonDataFrame):
                entities = TectonDataFrame._create(entities)
            assert set(entities._dataframe.columns).issubset(
                set(fd.join_keys)
            ), f"Entities should only contain columns that can be used as Join Keys: {fd.join_keys}"
            columns = entities.columns
            entities_df = SelectDistinctNode(UserSpecifiedDataNode(entities).as_ref(), columns).as_ref()
            qt = JoinNode(qt, entities_df, columns, how="right").as_ref()

        qt = FeatureTimeFilterNode(
            qt,
            feature_data_time_limits=time_range,
            policy=MaterializationTimeRangePolicy.MATERIALIZATION_TIME_RANGE_POLICY_FILTER_TO_RANGE,
            timestamp_field=fd.timestamp_key,
        ).as_ref()
        return TectonDataFrame._create(qt)
    else:
        # Validate that entities only contains Join Key Columns.
        if entities is not None:
            if isinstance(entities, pd.DataFrame):
                entities = spark.createDataFrame(entities)
            if isinstance(entities, TectonDataFrame):
                entities = entities.to_spark()
            assert set(entities.columns).issubset(
                set(fd.join_keys)
            ), f"Entities should only contain columns that can be used as Join Keys: {fd.join_keys}"
        try:
            batch_schedule_seconds = int(fd.fv.materialization_params.schedule_interval.ToTimedelta().total_seconds())
            data_delay_seconds = fd.online_store_data_delay_seconds
            if fd.is_temporal or fd.is_feature_table:
                df = aggregations.get_all_temporal_ft_features(spark, fd, entities, not from_source, time_range)
                if conf.get_bool("DATA_SKEW_REDUCTION"):
                    df = add_effective_timestamp(
                        df,
                        effective_timestamp_name=EFFECTIVE_TIMESTAMP,
                        batch_schedule_seconds=batch_schedule_seconds,
                        data_delay_seconds=data_delay_seconds,
                        timestamp_field=fd.timestamp_key,
                        is_stream=fd.is_stream,
                        is_temporal_aggregate=False,
                    )
            else:
                df = data_frame_helper._get_feature_dataframe_with_limits(
                    fd,
                    spine=None,
                    spine_time_limits=time_range,
                    use_materialized_data=not from_source,
                    spine_time_key=None,
                    validate_time_key=False,
                ).to_spark()
                if entities is not None:
                    df = df.join(functions.broadcast(entities.distinct()), entities.columns, how="right")
                columns = fd.join_keys + fd.features + [fd.timestamp_key]
                if conf.get_bool("DATA_SKEW_REDUCTION"):
                    df = add_effective_timestamp(
                        df,
                        effective_timestamp_name=EFFECTIVE_TIMESTAMP,
                        batch_schedule_seconds=batch_schedule_seconds,
                        data_delay_seconds=data_delay_seconds,
                        timestamp_field=fd.timestamp_key,
                        is_stream=fd.is_stream,
                        is_temporal_aggregate=True,
                    )
                    columns.append(EFFECTIVE_TIMESTAMP)
                df = df.select(*columns)
        except pyspark.sql.utils.AnalysisException as e:
            if "Unable to infer schema for Parquet" in e.desc or "doesn't exist" in e.desc:
                if fd.is_feature_table:
                    return TectonDataFrame._create(tc._spark.createDataFrame([], schema_to_spark(fd.view_schema)))
                else:
                    raise internal_errors.FV_NO_MATERIALIZED_DATA(fd.name)
            raise

        # Temporal feature views derived directly from raw data should already filtered to this timerange, but all other
        # cases may have data outside of this range. Apply this filter in all cases to be safe.
        if _start:
            df = df.filter(df[fd.timestamp_key] >= _start)
        if _end:
            df = df.filter(df[fd.timestamp_key] < _end)

        return TectonDataFrame._create(df)
