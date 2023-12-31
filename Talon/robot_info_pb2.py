# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: robot_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2
import geometry_pb2 as geometry__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10robot_info.proto\x12\x05rocos\x1a\x0cheader.proto\x1a\x0egeometry.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x88\x01\n\tJointInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x63nt_per_unit\x18\x02 \x01(\x01\x12\x17\n\x0ftorque_per_unit\x18\x03 \x01(\x01\x12\r\n\x05ratio\x18\x04 \x01(\x01\x12\x17\n\x0fpos_zero_offset\x18\x05 \x01(\x05\x12\x16\n\x0euser_unit_name\x18\x06 \x01(\t\"2\n\tRobotInfo\x12%\n\x0bjoint_infos\x18\x01 \x03(\x0b\x32\x10.rocos.JointInfo\"8\n\x10RobotInfoRequest\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.rocos.RequestHeader\"`\n\x11RobotInfoResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.rocos.ResponseHeader\x12$\n\nrobot_info\x18\x02 \x01(\x0b\x32\x10.rocos.RobotInfoB\x10\x42\x0eRobotInfoProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'robot_info_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\016RobotInfoProto'
  _globals['_JOINTINFO']._serialized_start=123
  _globals['_JOINTINFO']._serialized_end=259
  _globals['_ROBOTINFO']._serialized_start=261
  _globals['_ROBOTINFO']._serialized_end=311
  _globals['_ROBOTINFOREQUEST']._serialized_start=313
  _globals['_ROBOTINFOREQUEST']._serialized_end=369
  _globals['_ROBOTINFORESPONSE']._serialized_start=371
  _globals['_ROBOTINFORESPONSE']._serialized_end=467
# @@protoc_insertion_point(module_scope)
