# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/common/schema.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tecton_proto.common import column_type_pb2 as tecton__proto_dot_common_dot_column__type__pb2
from tecton_proto.common import data_type_pb2 as tecton__proto_dot_common_dot_data__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n tecton_proto/common/schema.proto\x12\x13tecton_proto.common\x1a%tecton_proto/common/column_type.proto\x1a#tecton_proto/common/data_type.proto\"\xe4\x02\n\x06\x43olumn\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12$\n\x0eraw_spark_type\x18\x02 \x01(\tR\x0crawSparkType\x12,\n\x12raw_snowflake_type\x18\x04 \x01(\tR\x10rawSnowflakeType\x12O\n\x13\x66\x65\x61ture_server_type\x18\x03 \x01(\x0e\x32\x1f.tecton_proto.common.ColumnTypeR\x11\x66\x65\x61tureServerType\x12I\n\x11offline_data_type\x18\x05 \x01(\x0b\x32\x1d.tecton_proto.common.DataTypeR\x0fofflineDataType\x12V\n\x18\x66\x65\x61ture_server_data_type\x18\x06 \x01(\x0b\x32\x1d.tecton_proto.common.DataTypeR\x15\x66\x65\x61tureServerDataType\"E\n\x06Schema\x12\x35\n\x07\x63olumns\x18\x02 \x03(\x0b\x32\x1b.tecton_proto.common.ColumnR\x07\x63olumnsJ\x04\x08\x01\x10\x02\x42\x15\n\x11\x63om.tecton.commonP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.common.schema_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021com.tecton.commonP\001'
  _COLUMN._serialized_start=134
  _COLUMN._serialized_end=490
  _SCHEMA._serialized_start=492
  _SCHEMA._serialized_end=561
# @@protoc_insertion_point(module_scope)
