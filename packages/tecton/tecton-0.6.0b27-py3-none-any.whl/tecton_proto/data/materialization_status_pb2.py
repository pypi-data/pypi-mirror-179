# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/data/materialization_status.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from tecton_proto.common import id_pb2 as tecton__proto_dot_common_dot_id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.tecton_proto/data/materialization_status.proto\x12\x11tecton_proto.data\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1ctecton_proto/common/id.proto\"\xd0\x0b\n\x1cMaterializationAttemptStatus\x12K\n\x10\x64\x61ta_source_type\x18\x01 \x01(\x0e\x32!.tecton_proto.data.DataSourceTypeR\x0e\x64\x61taSourceType\x12\x46\n\x11window_start_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0fwindowStartTime\x12\x42\n\x0fwindow_end_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rwindowEndTime\x12H\n\x12\x66\x65\x61ture_start_time\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x10\x66\x65\x61tureStartTime\x12\x44\n\x10\x66\x65\x61ture_end_time\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0e\x66\x65\x61tureEndTime\x12\x62\n\x15materialization_state\x18\x04 \x01(\x0e\x32-.tecton_proto.data.MaterializationStatusStateR\x14materializationState\x12#\n\rstate_message\x18\n \x01(\tR\x0cstateMessage\x12-\n\x12termination_reason\x18\x0b \x01(\tR\x11terminationReason\x12\x32\n\x15spot_instance_failure\x18\x0c \x01(\x08R\x13spotInstanceFailure\x12O\n\x17materialization_task_id\x18\x05 \x01(\x0b\x32\x17.tecton_proto.common.IdR\x15materializationTaskId\x12\x61\n\x1fmaterialization_task_created_at\x18\r \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x1cmaterializationTaskCreatedAt\x12%\n\x0e\x61ttempt_number\x18\x06 \x01(\x05R\rattemptNumber\x12I\n!spark_cluster_environment_version\x18\x07 \x01(\x05R\x1esparkClusterEnvironmentVersion\x12 \n\x0crun_page_url\x18\x08 \x01(\tR\nrunPageUrl\x12H\n\x12\x61ttempt_created_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x10\x61ttemptCreatedAt\x12\x30\n\x14is_permanent_failure\x18\x10 \x01(\x08R\x12isPermanentFailure\x12\x39\n\nretry_time\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tretryTime\x12\x1a\n\x08progress\x18\x12 \x01(\x02R\x08progress\x12\x35\n\x08\x64uration\x18\x13 \x01(\x0b\x32\x19.google.protobuf.DurationR\x08\x64uration\x12,\n\x12\x61llow_forced_retry\x18\x14 \x01(\x08R\x10\x61llowForcedRetry\x12\x32\n\x15\x61llow_overwrite_retry\x18\x15 \x01(\x08R\x13\x61llowOverwriteRetry\x12!\n\x0c\x61llow_cancel\x18\x16 \x01(\x08R\x0b\x61llowCancel\x12@\n\x1dwrite_to_online_feature_store\x18\x17 \x01(\x08R\x19writeToOnlineFeatureStore\x12\x42\n\x1ewrite_to_offline_feature_store\x18\x18 \x01(\x08R\x1awriteToOfflineFeatureStore\"\xca\x01\n\x15MaterializationStatus\x12\x45\n\x12\x66\x65\x61ture_package_id\x18\x01 \x01(\x0b\x32\x17.tecton_proto.common.IdR\x10\x66\x65\x61turePackageId\x12j\n\x18materialization_attempts\x18\x02 \x03(\x0b\x32/.tecton_proto.data.MaterializationAttemptStatusR\x17materializationAttempts*\xa3\x01\n\x0e\x44\x61taSourceType\x12\x1c\n\x18\x44\x41TA_SOURCE_TYPE_UNKNOWN\x10\x00\x12\x1a\n\x16\x44\x41TA_SOURCE_TYPE_BATCH\x10\x01\x12\x1b\n\x17\x44\x41TA_SOURCE_TYPE_STREAM\x10\x02\x12\x1b\n\x17\x44\x41TA_SOURCE_TYPE_INGEST\x10\x03\x12\x1d\n\x19\x44\x41TA_SOURCE_TYPE_DELETION\x10\x04*\xb7\x03\n\x1aMaterializationStatusState\x12(\n$MATERIALIZATION_STATUS_STATE_UNKNOWN\x10\x00\x12*\n&MATERIALIZATION_STATUS_STATE_SCHEDULED\x10\x01\x12(\n$MATERIALIZATION_STATUS_STATE_PENDING\x10\x02\x12(\n$MATERIALIZATION_STATUS_STATE_RUNNING\x10\x03\x12(\n$MATERIALIZATION_STATUS_STATE_SUCCESS\x10\x04\x12&\n\"MATERIALIZATION_STATUS_STATE_ERROR\x10\x05\x12(\n$MATERIALIZATION_STATUS_STATE_DRAINED\x10\x06\x12>\n:MATERIALIZATION_STATUS_STATE_MANUAL_CANCELLATION_REQUESTED\x10\x07\x12\x33\n/MATERIALIZATION_STATUS_STATE_MANUALLY_CANCELLED\x10\x08\x42\x13\n\x0f\x63om.tecton.dataP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.data.materialization_status_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.tecton.dataP\001'
  _DATASOURCETYPE._serialized_start=1861
  _DATASOURCETYPE._serialized_end=2024
  _MATERIALIZATIONSTATUSSTATE._serialized_start=2027
  _MATERIALIZATIONSTATUSSTATE._serialized_end=2466
  _MATERIALIZATIONATTEMPTSTATUS._serialized_start=165
  _MATERIALIZATIONATTEMPTSTATUS._serialized_end=1653
  _MATERIALIZATIONSTATUS._serialized_start=1656
  _MATERIALIZATIONSTATUS._serialized_end=1858
# @@protoc_insertion_point(module_scope)
