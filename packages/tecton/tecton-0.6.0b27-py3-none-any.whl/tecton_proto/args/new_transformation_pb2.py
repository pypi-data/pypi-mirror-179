# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/args/new_transformation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tecton_proto.args import user_defined_function_pb2 as tecton__proto_dot_args_dot_user__defined__function__pb2
from tecton_proto.args import basic_info_pb2 as tecton__proto_dot_args_dot_basic__info__pb2
from tecton_proto.common import id_pb2 as tecton__proto_dot_common_dot_id__pb2
from tecton_proto.args import diff_options_pb2 as tecton__proto_dot_args_dot_diff__options__pb2
from tecton_proto.common import framework_version_pb2 as tecton__proto_dot_common_dot_framework__version__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*tecton_proto/args/new_transformation.proto\x12\x11tecton_proto.args\x1a-tecton_proto/args/user_defined_function.proto\x1a\"tecton_proto/args/basic_info.proto\x1a\x1ctecton_proto/common/id.proto\x1a$tecton_proto/args/diff_options.proto\x1a+tecton_proto/common/framework_version.proto\"\xd5\x03\n\x15NewTransformationArgs\x12\x44\n\x11transformation_id\x18\x01 \x01(\x0b\x32\x17.tecton_proto.common.IdR\x10transformationId\x12\x37\n\x04info\x18\x02 \x01(\x0b\x32\x1c.tecton_proto.args.BasicInfoB\x05\x92M\x02\x10\x01R\x04info\x12\x46\n\x07version\x18\x07 \x01(\x0e\x32%.tecton_proto.common.FrameworkVersionB\x05\x92M\x02\x08\x05R\x07version\x12]\n\x13transformation_mode\x18\x03 \x01(\x0e\x32%.tecton_proto.args.TransformationModeB\x05\x92M\x02\x08\x06R\x12transformationMode\x12R\n\ruser_function\x18\x04 \x01(\x0b\x32&.tecton_proto.args.UserDefinedFunctionB\x05\x92M\x02\x08\x06R\x0cuserFunction\x12#\n\tdocstring\x18\x06 \x01(\tB\x05\x92M\x02\x08\x01R\tdocstring\x12\x1d\n\nis_builtin\x18\x05 \x01(\x08R\tisBuiltin*\xa2\x02\n\x12TransformationMode\x12\x1f\n\x1bTRANSFORMATION_MODE_UNKNOWN\x10\x00\x12\x1f\n\x1bTRANSFORMATION_MODE_PYSPARK\x10\x01\x12!\n\x1dTRANSFORMATION_MODE_SPARK_SQL\x10\x02\x12\x1e\n\x1aTRANSFORMATION_MODE_PANDAS\x10\x03\x12%\n!TRANSFORMATION_MODE_SNOWFLAKE_SQL\x10\x04\x12\x1e\n\x1aTRANSFORMATION_MODE_PYTHON\x10\x05\x12 \n\x1cTRANSFORMATION_MODE_SNOWPARK\x10\x06\x12\x1e\n\x1aTRANSFORMATION_MODE_ATHENA\x10\x07\x42\x13\n\x0f\x63om.tecton.argsP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.args.new_transformation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.tecton.argsP\001'
  _NEWTRANSFORMATIONARGS.fields_by_name['info']._options = None
  _NEWTRANSFORMATIONARGS.fields_by_name['info']._serialized_options = b'\222M\002\020\001'
  _NEWTRANSFORMATIONARGS.fields_by_name['version']._options = None
  _NEWTRANSFORMATIONARGS.fields_by_name['version']._serialized_options = b'\222M\002\010\005'
  _NEWTRANSFORMATIONARGS.fields_by_name['transformation_mode']._options = None
  _NEWTRANSFORMATIONARGS.fields_by_name['transformation_mode']._serialized_options = b'\222M\002\010\006'
  _NEWTRANSFORMATIONARGS.fields_by_name['user_function']._options = None
  _NEWTRANSFORMATIONARGS.fields_by_name['user_function']._serialized_options = b'\222M\002\010\006'
  _NEWTRANSFORMATIONARGS.fields_by_name['docstring']._options = None
  _NEWTRANSFORMATIONARGS.fields_by_name['docstring']._serialized_options = b'\222M\002\010\001'
  _TRANSFORMATIONMODE._serialized_start=734
  _TRANSFORMATIONMODE._serialized_end=1024
  _NEWTRANSFORMATIONARGS._serialized_start=262
  _NEWTRANSFORMATIONARGS._serialized_end=731
# @@protoc_insertion_point(module_scope)
