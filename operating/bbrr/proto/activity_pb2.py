# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: activity.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import protocommon_pb2
import rescommon_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='activity.proto',
  package='',
  serialized_pb=_b('\n\x0e\x61\x63tivity.proto\x1a\x11protocommon.proto\x1a\x0frescommon.proto\"\x9e\x01\n\x1fSCDT_ACTIVITY_RESOURCE_BOX_INFO\x12\x1d\n\x15last_box_refresh_time\x18\x01 \x01(\r\x12\x1b\n\x13gold_box_open_count\x18\x02 \x01(\r\x12\x1e\n\x16\x63rystal_box_open_count\x18\x04 \x01(\r\x12\x1f\n\x17material_box_open_count\x18\x06 \x01(\r\"\xb6\x02\n\x12SCDT_ACTIVITY_INFO\x12\x34\n\x12\x63umulate_cost_info\x18\x01 \x01(\x0b\x32\x18.SCDT_CUMULATE_COST_INFO\x12\x34\n\x12sect_recharge_info\x18\x02 \x01(\x0b\x32\x18.SCDT_SECT_RECHARGE_INFO\x12\x36\n\x13\x64\x61ily_recharge_info\x18\x03 \x01(\x0b\x32\x19.SCDT_DAILY_RECHARGE_INFO\x12;\n\x13\x61\x63tivity_prize_draw\x18\x04 \x01(\x0b\x32\x1e.SCDT_ACTIVITY_PRIZE_DRAW_INFO\x12?\n\x15\x61\x63tivity_resource_box\x18\x05 \x01(\x0b\x32 .SCDT_ACTIVITY_RESOURCE_BOX_INFO\"U\n\x15SCDT_ACTIVITY_CONTROL\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04stat\x18\x02 \x01(\r\x12\x10\n\x08\x62\x65g_time\x18\x03 \x01(\r\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\r\"\'\n\x17\x43SDT_ACTIVITY_BROADCAST\x12\x0c\n\x04info\x18\x01 \x01(\t\"W\n\x1e\x43SDT_ACTIVITY_STATUS_BROADCAST\x12\x13\n\x0b\x61\x63tivity_id\x18\x01 \x01(\r\x12\x0e\n\x06status\x18\x02 \x01(\r\x12\x10\n\x08hint_msg\x18\x03 \x01(\t\"e\n\x16SCPKG_ACTIVITY_CONTROL\x12\x30\n\x10\x61\x63tivity_control\x18\x01 \x01(\x0b\x32\x16.SCDT_ACTIVITY_CONTROL\x12\x19\n\x11is_world_activity\x18\x02 \x01(\x08\"\xab\x01\n\x13SCPKG_ACTIVITY_INFO\x12\x30\n\x10\x61\x63tivity_control\x18\x01 \x03(\x0b\x32\x16.SCDT_ACTIVITY_CONTROL\x12*\n\ractivity_info\x18\x02 \x01(\x0b\x32\x13.SCDT_ACTIVITY_INFO\x12\x36\n\x16world_activity_control\x18\x03 \x03(\x0b\x32\x16.SCDT_ACTIVITY_CONTROL\"\xa3\x01\n\x0e\x43SDT_BROAD_MSG\x12\x0e\n\x06gm_msg\x18\x01 \x01(\t\x12\x30\n\x0e\x62road_activity\x18\x02 \x01(\x0b\x32\x18.CSDT_ACTIVITY_BROADCAST\x12>\n\x15\x62road_activity_status\x18\x03 \x01(\x0b\x32\x1f.CSDT_ACTIVITY_STATUS_BROADCAST\x12\x0f\n\x07reserve\x18\x04 \x01(\x05\"[\n\x13SCPKG_NTF_BROADCAST\x12\x0e\n\x06msg_id\x18\x01 \x01(\r\x12\x10\n\x08show_pos\x18\x02 \x01(\r\x12\"\n\tbroad_msg\x18\x03 \x01(\x0b\x32\x0f.CSDT_BROAD_MSG\"A\n\"SCPKG_GAME_PLAY_MODE_ACTIVITY_INFO\x12\x1b\n\x13\x63losed_dungeon_type\x18\x01 \x03(\r\"+\n\x1b\x43SPKG_OPEN_RESOURCE_BOX_REQ\x12\x0c\n\x04type\x18\x01 \x01(\r\"W\n\x1bSCPKG_OPEN_RESOURCE_BOX_RES\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\r\x12\x1a\n\x06reward\x18\x03 \x03(\x0b\x32\n.ResReward\"c\n SCPKG_ACTIVITY_RESOURCE_BOX_INFO\x12?\n\x15\x61\x63tivity_resource_box\x18\x01 \x01(\x0b\x32 .SCDT_ACTIVITY_RESOURCE_BOX_INFO\"9\n\x1d\x43SPKG_GET_COUNT_TO_REWARD_REQ\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\n\n\x02id\x18\x02 \x01(\r\"e\n\x1dSCPKG_GET_COUNT_TO_REWARD_RES\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\r\x12\n\n\x02id\x18\x03 \x01(\r\x12\x1a\n\x06reward\x18\x04 \x03(\x0b\x32\n.ResReward\"\x95\x01\n\x1bSCPKG_NTF_ACTIVITY_DISCOUNT\x12\x1c\n\x14\x63oin_single_discount\x18\x01 \x01(\r\x12\x1b\n\x13\x63oin_multi_discount\x18\x02 \x01(\r\x12\x1d\n\x15money_single_discount\x18\x03 \x01(\r\x12\x1c\n\x14money_multi_discount\x18\x04 \x01(\r')
  ,
  dependencies=[protocommon_pb2.DESCRIPTOR,rescommon_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SCDT_ACTIVITY_RESOURCE_BOX_INFO = _descriptor.Descriptor(
  name='SCDT_ACTIVITY_RESOURCE_BOX_INFO',
  full_name='SCDT_ACTIVITY_RESOURCE_BOX_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='last_box_refresh_time', full_name='SCDT_ACTIVITY_RESOURCE_BOX_INFO.last_box_refresh_time', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold_box_open_count', full_name='SCDT_ACTIVITY_RESOURCE_BOX_INFO.gold_box_open_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crystal_box_open_count', full_name='SCDT_ACTIVITY_RESOURCE_BOX_INFO.crystal_box_open_count', index=2,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='material_box_open_count', full_name='SCDT_ACTIVITY_RESOURCE_BOX_INFO.material_box_open_count', index=3,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=55,
  serialized_end=213,
)


_SCDT_ACTIVITY_INFO = _descriptor.Descriptor(
  name='SCDT_ACTIVITY_INFO',
  full_name='SCDT_ACTIVITY_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cumulate_cost_info', full_name='SCDT_ACTIVITY_INFO.cumulate_cost_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sect_recharge_info', full_name='SCDT_ACTIVITY_INFO.sect_recharge_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='daily_recharge_info', full_name='SCDT_ACTIVITY_INFO.daily_recharge_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activity_prize_draw', full_name='SCDT_ACTIVITY_INFO.activity_prize_draw', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activity_resource_box', full_name='SCDT_ACTIVITY_INFO.activity_resource_box', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=216,
  serialized_end=526,
)


_SCDT_ACTIVITY_CONTROL = _descriptor.Descriptor(
  name='SCDT_ACTIVITY_CONTROL',
  full_name='SCDT_ACTIVITY_CONTROL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SCDT_ACTIVITY_CONTROL.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stat', full_name='SCDT_ACTIVITY_CONTROL.stat', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beg_time', full_name='SCDT_ACTIVITY_CONTROL.beg_time', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='SCDT_ACTIVITY_CONTROL.end_time', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=528,
  serialized_end=613,
)


_CSDT_ACTIVITY_BROADCAST = _descriptor.Descriptor(
  name='CSDT_ACTIVITY_BROADCAST',
  full_name='CSDT_ACTIVITY_BROADCAST',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='CSDT_ACTIVITY_BROADCAST.info', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=615,
  serialized_end=654,
)


_CSDT_ACTIVITY_STATUS_BROADCAST = _descriptor.Descriptor(
  name='CSDT_ACTIVITY_STATUS_BROADCAST',
  full_name='CSDT_ACTIVITY_STATUS_BROADCAST',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activity_id', full_name='CSDT_ACTIVITY_STATUS_BROADCAST.activity_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='CSDT_ACTIVITY_STATUS_BROADCAST.status', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hint_msg', full_name='CSDT_ACTIVITY_STATUS_BROADCAST.hint_msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=656,
  serialized_end=743,
)


_SCPKG_ACTIVITY_CONTROL = _descriptor.Descriptor(
  name='SCPKG_ACTIVITY_CONTROL',
  full_name='SCPKG_ACTIVITY_CONTROL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activity_control', full_name='SCPKG_ACTIVITY_CONTROL.activity_control', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_world_activity', full_name='SCPKG_ACTIVITY_CONTROL.is_world_activity', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=745,
  serialized_end=846,
)


_SCPKG_ACTIVITY_INFO = _descriptor.Descriptor(
  name='SCPKG_ACTIVITY_INFO',
  full_name='SCPKG_ACTIVITY_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activity_control', full_name='SCPKG_ACTIVITY_INFO.activity_control', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activity_info', full_name='SCPKG_ACTIVITY_INFO.activity_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='world_activity_control', full_name='SCPKG_ACTIVITY_INFO.world_activity_control', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=849,
  serialized_end=1020,
)


_CSDT_BROAD_MSG = _descriptor.Descriptor(
  name='CSDT_BROAD_MSG',
  full_name='CSDT_BROAD_MSG',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gm_msg', full_name='CSDT_BROAD_MSG.gm_msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='broad_activity', full_name='CSDT_BROAD_MSG.broad_activity', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='broad_activity_status', full_name='CSDT_BROAD_MSG.broad_activity_status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reserve', full_name='CSDT_BROAD_MSG.reserve', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1023,
  serialized_end=1186,
)


_SCPKG_NTF_BROADCAST = _descriptor.Descriptor(
  name='SCPKG_NTF_BROADCAST',
  full_name='SCPKG_NTF_BROADCAST',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='SCPKG_NTF_BROADCAST.msg_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='show_pos', full_name='SCPKG_NTF_BROADCAST.show_pos', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='broad_msg', full_name='SCPKG_NTF_BROADCAST.broad_msg', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1188,
  serialized_end=1279,
)


_SCPKG_GAME_PLAY_MODE_ACTIVITY_INFO = _descriptor.Descriptor(
  name='SCPKG_GAME_PLAY_MODE_ACTIVITY_INFO',
  full_name='SCPKG_GAME_PLAY_MODE_ACTIVITY_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='closed_dungeon_type', full_name='SCPKG_GAME_PLAY_MODE_ACTIVITY_INFO.closed_dungeon_type', index=0,
      number=1, type=13, cpp_type=3, label=3,
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
  serialized_start=1281,
  serialized_end=1346,
)


_CSPKG_OPEN_RESOURCE_BOX_REQ = _descriptor.Descriptor(
  name='CSPKG_OPEN_RESOURCE_BOX_REQ',
  full_name='CSPKG_OPEN_RESOURCE_BOX_REQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='CSPKG_OPEN_RESOURCE_BOX_REQ.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1348,
  serialized_end=1391,
)


_SCPKG_OPEN_RESOURCE_BOX_RES = _descriptor.Descriptor(
  name='SCPKG_OPEN_RESOURCE_BOX_RES',
  full_name='SCPKG_OPEN_RESOURCE_BOX_RES',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SCPKG_OPEN_RESOURCE_BOX_RES.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='SCPKG_OPEN_RESOURCE_BOX_RES.type', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward', full_name='SCPKG_OPEN_RESOURCE_BOX_RES.reward', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=1393,
  serialized_end=1480,
)


_SCPKG_ACTIVITY_RESOURCE_BOX_INFO = _descriptor.Descriptor(
  name='SCPKG_ACTIVITY_RESOURCE_BOX_INFO',
  full_name='SCPKG_ACTIVITY_RESOURCE_BOX_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activity_resource_box', full_name='SCPKG_ACTIVITY_RESOURCE_BOX_INFO.activity_resource_box', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1482,
  serialized_end=1581,
)


_CSPKG_GET_COUNT_TO_REWARD_REQ = _descriptor.Descriptor(
  name='CSPKG_GET_COUNT_TO_REWARD_REQ',
  full_name='CSPKG_GET_COUNT_TO_REWARD_REQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='CSPKG_GET_COUNT_TO_REWARD_REQ.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='CSPKG_GET_COUNT_TO_REWARD_REQ.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1583,
  serialized_end=1640,
)


_SCPKG_GET_COUNT_TO_REWARD_RES = _descriptor.Descriptor(
  name='SCPKG_GET_COUNT_TO_REWARD_RES',
  full_name='SCPKG_GET_COUNT_TO_REWARD_RES',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SCPKG_GET_COUNT_TO_REWARD_RES.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='SCPKG_GET_COUNT_TO_REWARD_RES.type', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='SCPKG_GET_COUNT_TO_REWARD_RES.id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward', full_name='SCPKG_GET_COUNT_TO_REWARD_RES.reward', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=1642,
  serialized_end=1743,
)


_SCPKG_NTF_ACTIVITY_DISCOUNT = _descriptor.Descriptor(
  name='SCPKG_NTF_ACTIVITY_DISCOUNT',
  full_name='SCPKG_NTF_ACTIVITY_DISCOUNT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coin_single_discount', full_name='SCPKG_NTF_ACTIVITY_DISCOUNT.coin_single_discount', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coin_multi_discount', full_name='SCPKG_NTF_ACTIVITY_DISCOUNT.coin_multi_discount', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='money_single_discount', full_name='SCPKG_NTF_ACTIVITY_DISCOUNT.money_single_discount', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='money_multi_discount', full_name='SCPKG_NTF_ACTIVITY_DISCOUNT.money_multi_discount', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1746,
  serialized_end=1895,
)

_SCDT_ACTIVITY_INFO.fields_by_name['cumulate_cost_info'].message_type = protocommon_pb2._SCDT_CUMULATE_COST_INFO
_SCDT_ACTIVITY_INFO.fields_by_name['sect_recharge_info'].message_type = protocommon_pb2._SCDT_SECT_RECHARGE_INFO
_SCDT_ACTIVITY_INFO.fields_by_name['daily_recharge_info'].message_type = protocommon_pb2._SCDT_DAILY_RECHARGE_INFO
_SCDT_ACTIVITY_INFO.fields_by_name['activity_prize_draw'].message_type = protocommon_pb2._SCDT_ACTIVITY_PRIZE_DRAW_INFO
_SCDT_ACTIVITY_INFO.fields_by_name['activity_resource_box'].message_type = _SCDT_ACTIVITY_RESOURCE_BOX_INFO
_SCPKG_ACTIVITY_CONTROL.fields_by_name['activity_control'].message_type = _SCDT_ACTIVITY_CONTROL
_SCPKG_ACTIVITY_INFO.fields_by_name['activity_control'].message_type = _SCDT_ACTIVITY_CONTROL
_SCPKG_ACTIVITY_INFO.fields_by_name['activity_info'].message_type = _SCDT_ACTIVITY_INFO
_SCPKG_ACTIVITY_INFO.fields_by_name['world_activity_control'].message_type = _SCDT_ACTIVITY_CONTROL
_CSDT_BROAD_MSG.fields_by_name['broad_activity'].message_type = _CSDT_ACTIVITY_BROADCAST
_CSDT_BROAD_MSG.fields_by_name['broad_activity_status'].message_type = _CSDT_ACTIVITY_STATUS_BROADCAST
_SCPKG_NTF_BROADCAST.fields_by_name['broad_msg'].message_type = _CSDT_BROAD_MSG
_SCPKG_OPEN_RESOURCE_BOX_RES.fields_by_name['reward'].message_type = rescommon_pb2._RESREWARD
_SCPKG_ACTIVITY_RESOURCE_BOX_INFO.fields_by_name['activity_resource_box'].message_type = _SCDT_ACTIVITY_RESOURCE_BOX_INFO
_SCPKG_GET_COUNT_TO_REWARD_RES.fields_by_name['reward'].message_type = rescommon_pb2._RESREWARD
DESCRIPTOR.message_types_by_name['SCDT_ACTIVITY_RESOURCE_BOX_INFO'] = _SCDT_ACTIVITY_RESOURCE_BOX_INFO
DESCRIPTOR.message_types_by_name['SCDT_ACTIVITY_INFO'] = _SCDT_ACTIVITY_INFO
DESCRIPTOR.message_types_by_name['SCDT_ACTIVITY_CONTROL'] = _SCDT_ACTIVITY_CONTROL
DESCRIPTOR.message_types_by_name['CSDT_ACTIVITY_BROADCAST'] = _CSDT_ACTIVITY_BROADCAST
DESCRIPTOR.message_types_by_name['CSDT_ACTIVITY_STATUS_BROADCAST'] = _CSDT_ACTIVITY_STATUS_BROADCAST
DESCRIPTOR.message_types_by_name['SCPKG_ACTIVITY_CONTROL'] = _SCPKG_ACTIVITY_CONTROL
DESCRIPTOR.message_types_by_name['SCPKG_ACTIVITY_INFO'] = _SCPKG_ACTIVITY_INFO
DESCRIPTOR.message_types_by_name['CSDT_BROAD_MSG'] = _CSDT_BROAD_MSG
DESCRIPTOR.message_types_by_name['SCPKG_NTF_BROADCAST'] = _SCPKG_NTF_BROADCAST
DESCRIPTOR.message_types_by_name['SCPKG_GAME_PLAY_MODE_ACTIVITY_INFO'] = _SCPKG_GAME_PLAY_MODE_ACTIVITY_INFO
DESCRIPTOR.message_types_by_name['CSPKG_OPEN_RESOURCE_BOX_REQ'] = _CSPKG_OPEN_RESOURCE_BOX_REQ
DESCRIPTOR.message_types_by_name['SCPKG_OPEN_RESOURCE_BOX_RES'] = _SCPKG_OPEN_RESOURCE_BOX_RES
DESCRIPTOR.message_types_by_name['SCPKG_ACTIVITY_RESOURCE_BOX_INFO'] = _SCPKG_ACTIVITY_RESOURCE_BOX_INFO
DESCRIPTOR.message_types_by_name['CSPKG_GET_COUNT_TO_REWARD_REQ'] = _CSPKG_GET_COUNT_TO_REWARD_REQ
DESCRIPTOR.message_types_by_name['SCPKG_GET_COUNT_TO_REWARD_RES'] = _SCPKG_GET_COUNT_TO_REWARD_RES
DESCRIPTOR.message_types_by_name['SCPKG_NTF_ACTIVITY_DISCOUNT'] = _SCPKG_NTF_ACTIVITY_DISCOUNT

SCDT_ACTIVITY_RESOURCE_BOX_INFO = _reflection.GeneratedProtocolMessageType('SCDT_ACTIVITY_RESOURCE_BOX_INFO', (_message.Message,), dict(
  DESCRIPTOR = _SCDT_ACTIVITY_RESOURCE_BOX_INFO,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:SCDT_ACTIVITY_RESOURCE_BOX_INFO)
  ))
_sym_db.RegisterMessage(SCDT_ACTIVITY_RESOURCE_BOX_INFO)

SCDT_ACTIVITY_INFO = _reflection.GeneratedProtocolMessageType('SCDT_ACTIVITY_INFO', (_message.Message,), dict(
  DESCRIPTOR = _SCDT_ACTIVITY_INFO,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:SCDT_ACTIVITY_INFO)
  ))
_sym_db.RegisterMessage(SCDT_ACTIVITY_INFO)

SCDT_ACTIVITY_CONTROL = _reflection.GeneratedProtocolMessageType('SCDT_ACTIVITY_CONTROL', (_message.Message,), dict(
  DESCRIPTOR = _SCDT_ACTIVITY_CONTROL,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:SCDT_ACTIVITY_CONTROL)
  ))
_sym_db.RegisterMessage(SCDT_ACTIVITY_CONTROL)

CSDT_ACTIVITY_BROADCAST = _reflection.GeneratedProtocolMessageType('CSDT_ACTIVITY_BROADCAST', (_message.Message,), dict(
  DESCRIPTOR = _CSDT_ACTIVITY_BROADCAST,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:CSDT_ACTIVITY_BROADCAST)
  ))
_sym_db.RegisterMessage(CSDT_ACTIVITY_BROADCAST)

CSDT_ACTIVITY_STATUS_BROADCAST = _reflection.GeneratedProtocolMessageType('CSDT_ACTIVITY_STATUS_BROADCAST', (_message.Message,), dict(
  DESCRIPTOR = _CSDT_ACTIVITY_STATUS_BROADCAST,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:CSDT_ACTIVITY_STATUS_BROADCAST)
  ))
_sym_db.RegisterMessage(CSDT_ACTIVITY_STATUS_BROADCAST)

SCPKG_ACTIVITY_CONTROL = _reflection.GeneratedProtocolMessageType('SCPKG_ACTIVITY_CONTROL', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_ACTIVITY_CONTROL,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_ACTIVITY_CONTROL)
  ))
_sym_db.RegisterMessage(SCPKG_ACTIVITY_CONTROL)

SCPKG_ACTIVITY_INFO = _reflection.GeneratedProtocolMessageType('SCPKG_ACTIVITY_INFO', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_ACTIVITY_INFO,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_ACTIVITY_INFO)
  ))
_sym_db.RegisterMessage(SCPKG_ACTIVITY_INFO)

CSDT_BROAD_MSG = _reflection.GeneratedProtocolMessageType('CSDT_BROAD_MSG', (_message.Message,), dict(
  DESCRIPTOR = _CSDT_BROAD_MSG,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:CSDT_BROAD_MSG)
  ))
_sym_db.RegisterMessage(CSDT_BROAD_MSG)

SCPKG_NTF_BROADCAST = _reflection.GeneratedProtocolMessageType('SCPKG_NTF_BROADCAST', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_NTF_BROADCAST,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_NTF_BROADCAST)
  ))
_sym_db.RegisterMessage(SCPKG_NTF_BROADCAST)

SCPKG_GAME_PLAY_MODE_ACTIVITY_INFO = _reflection.GeneratedProtocolMessageType('SCPKG_GAME_PLAY_MODE_ACTIVITY_INFO', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_GAME_PLAY_MODE_ACTIVITY_INFO,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_GAME_PLAY_MODE_ACTIVITY_INFO)
  ))
_sym_db.RegisterMessage(SCPKG_GAME_PLAY_MODE_ACTIVITY_INFO)

CSPKG_OPEN_RESOURCE_BOX_REQ = _reflection.GeneratedProtocolMessageType('CSPKG_OPEN_RESOURCE_BOX_REQ', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_OPEN_RESOURCE_BOX_REQ,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_OPEN_RESOURCE_BOX_REQ)
  ))
_sym_db.RegisterMessage(CSPKG_OPEN_RESOURCE_BOX_REQ)

SCPKG_OPEN_RESOURCE_BOX_RES = _reflection.GeneratedProtocolMessageType('SCPKG_OPEN_RESOURCE_BOX_RES', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_OPEN_RESOURCE_BOX_RES,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_OPEN_RESOURCE_BOX_RES)
  ))
_sym_db.RegisterMessage(SCPKG_OPEN_RESOURCE_BOX_RES)

SCPKG_ACTIVITY_RESOURCE_BOX_INFO = _reflection.GeneratedProtocolMessageType('SCPKG_ACTIVITY_RESOURCE_BOX_INFO', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_ACTIVITY_RESOURCE_BOX_INFO,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_ACTIVITY_RESOURCE_BOX_INFO)
  ))
_sym_db.RegisterMessage(SCPKG_ACTIVITY_RESOURCE_BOX_INFO)

CSPKG_GET_COUNT_TO_REWARD_REQ = _reflection.GeneratedProtocolMessageType('CSPKG_GET_COUNT_TO_REWARD_REQ', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_GET_COUNT_TO_REWARD_REQ,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_GET_COUNT_TO_REWARD_REQ)
  ))
_sym_db.RegisterMessage(CSPKG_GET_COUNT_TO_REWARD_REQ)

SCPKG_GET_COUNT_TO_REWARD_RES = _reflection.GeneratedProtocolMessageType('SCPKG_GET_COUNT_TO_REWARD_RES', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_GET_COUNT_TO_REWARD_RES,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_GET_COUNT_TO_REWARD_RES)
  ))
_sym_db.RegisterMessage(SCPKG_GET_COUNT_TO_REWARD_RES)

SCPKG_NTF_ACTIVITY_DISCOUNT = _reflection.GeneratedProtocolMessageType('SCPKG_NTF_ACTIVITY_DISCOUNT', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_NTF_ACTIVITY_DISCOUNT,
  __module__ = 'activity_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_NTF_ACTIVITY_DISCOUNT)
  ))
_sym_db.RegisterMessage(SCPKG_NTF_ACTIVITY_DISCOUNT)


# @@protoc_insertion_point(module_scope)
