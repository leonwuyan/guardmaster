# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cityreward.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import rescommon_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cityreward.proto',
  package='',
  serialized_pb=_b('\n\x10\x63ityreward.proto\x1a\x0frescommon.proto\"A\n\x1bNOTIFY_CITY_REWARD_ACQUIRED\x12\"\n\nrewardInfo\x18\x01 \x03(\x0b\x32\x0e.ResCityReward\"5\n\x0fREQ_CITY_REWARD\x12\"\n\nrewardInfo\x18\x01 \x02(\x0b\x32\x0e.ResCityReward\"E\n\x0fRES_CITY_REWARD\x12\x0e\n\x06result\x18\x01 \x02(\x05\x12\"\n\nrewardInfo\x18\x02 \x02(\x0b\x32\x0e.ResCityReward')
  ,
  dependencies=[rescommon_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_NOTIFY_CITY_REWARD_ACQUIRED = _descriptor.Descriptor(
  name='NOTIFY_CITY_REWARD_ACQUIRED',
  full_name='NOTIFY_CITY_REWARD_ACQUIRED',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewardInfo', full_name='NOTIFY_CITY_REWARD_ACQUIRED.rewardInfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=102,
)


_REQ_CITY_REWARD = _descriptor.Descriptor(
  name='REQ_CITY_REWARD',
  full_name='REQ_CITY_REWARD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewardInfo', full_name='REQ_CITY_REWARD.rewardInfo', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=157,
)


_RES_CITY_REWARD = _descriptor.Descriptor(
  name='RES_CITY_REWARD',
  full_name='RES_CITY_REWARD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='RES_CITY_REWARD.result', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rewardInfo', full_name='RES_CITY_REWARD.rewardInfo', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=228,
)

_NOTIFY_CITY_REWARD_ACQUIRED.fields_by_name['rewardInfo'].message_type = rescommon_pb2._RESCITYREWARD
_REQ_CITY_REWARD.fields_by_name['rewardInfo'].message_type = rescommon_pb2._RESCITYREWARD
_RES_CITY_REWARD.fields_by_name['rewardInfo'].message_type = rescommon_pb2._RESCITYREWARD
DESCRIPTOR.message_types_by_name['NOTIFY_CITY_REWARD_ACQUIRED'] = _NOTIFY_CITY_REWARD_ACQUIRED
DESCRIPTOR.message_types_by_name['REQ_CITY_REWARD'] = _REQ_CITY_REWARD
DESCRIPTOR.message_types_by_name['RES_CITY_REWARD'] = _RES_CITY_REWARD

NOTIFY_CITY_REWARD_ACQUIRED = _reflection.GeneratedProtocolMessageType('NOTIFY_CITY_REWARD_ACQUIRED', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFY_CITY_REWARD_ACQUIRED,
  __module__ = 'cityreward_pb2'
  # @@protoc_insertion_point(class_scope:NOTIFY_CITY_REWARD_ACQUIRED)
  ))
_sym_db.RegisterMessage(NOTIFY_CITY_REWARD_ACQUIRED)

REQ_CITY_REWARD = _reflection.GeneratedProtocolMessageType('REQ_CITY_REWARD', (_message.Message,), dict(
  DESCRIPTOR = _REQ_CITY_REWARD,
  __module__ = 'cityreward_pb2'
  # @@protoc_insertion_point(class_scope:REQ_CITY_REWARD)
  ))
_sym_db.RegisterMessage(REQ_CITY_REWARD)

RES_CITY_REWARD = _reflection.GeneratedProtocolMessageType('RES_CITY_REWARD', (_message.Message,), dict(
  DESCRIPTOR = _RES_CITY_REWARD,
  __module__ = 'cityreward_pb2'
  # @@protoc_insertion_point(class_scope:RES_CITY_REWARD)
  ))
_sym_db.RegisterMessage(RES_CITY_REWARD)


# @@protoc_insertion_point(module_scope)