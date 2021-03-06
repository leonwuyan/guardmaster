# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: viewplayer.proto

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
  name='viewplayer.proto',
  package='',
  serialized_pb=_b('\n\x10viewplayer.proto\x1a\x11protocommon.proto\x1a\x0frescommon.proto\"_\n\x1e\x43SPKG_CMD_VIEW_PLAYER_INFO_REQ\x12\x14\n\x0cview_role_id\x18\x01 \x01(\r\x12\x11\n\tvip_level\x18\x03 \x01(\r\x12\x14\n\x0cis_from_gang\x18\x02 \x01(\x08\"\xdb\x02\n\x18ST_VIEW_PlAYER_HERO_INFO\x12\x0f\n\x07hero_id\x18\x01 \x01(\r\x12\x0f\n\x07hero_lv\x18\x02 \x01(\r\x12\x14\n\x0chero_grow_up\x18\x03 \x01(\r\x12*\n\x0b\x65mblem_info\x18\x04 \x03(\x0b\x32\x15.CSDT_EMBLEMINFO_DATA\x12&\n\nequip_info\x18\x05 \x03(\x0b\x32\x12.CSDT_EQUIPED_INFO\x12\x1c\n\thero_attr\x18\x06 \x03(\x0b\x32\t.HeroAttr\x12\x13\n\x0btalent_info\x18\x07 \x01(\x04\x12:\n\x10talent_hide_info\x18\x08 \x03(\x0b\x32 .ST_HERO_BATTLE_TALENT_HIDE_INFO\x12\x16\n\x0etalent_lv_info\x18\t \x03(\r\x12\x17\n\x0f\x65quiped_factors\x18\n \x03(\r\x12\x13\n\x0b\x61wake_stage\x18\x0b \x01(\r\"\xe5\x03\n\x1eSCPKG_CMD_VIEW_PLAYER_INFO_RES\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x14\n\x0cis_from_gang\x18\x02 \x01(\x08\x12\x14\n\x0cview_role_id\x18\x03 \x01(\r\x12\x16\n\x0eview_role_name\x18\x04 \x01(\t\x12\x13\n\x0bpvp_win_cnt\x18\x05 \x01(\r\x12\x15\n\rpvp_total_cnt\x18\x06 \x01(\r\x12\x1b\n\x13greatest_dungeon_id\x18\x07 \x01(\r\x12\x11\n\tgang_name\x18\x08 \x01(\t\x12\x17\n\x0frank_battle_pos\x18\t \x01(\x05\x12\x15\n\rendless_floor\x18\n \x01(\r\x12\x1b\n\x13offline_battle_kill\x18\x0b \x01(\r\x12\x1c\n\x14\x61\x63hievement_rank_pos\x18\x0c \x01(\x05\x12\x34\n\x10gang_battle_info\x18\r \x01(\x0b\x32\x1a.CSDT_GANGBATTLE_HERO_INFO\x12,\n\thero_info\x18\x0e \x03(\x0b\x32\x19.ST_VIEW_PlAYER_HERO_INFO\x12\x11\n\tvip_level\x18\x0f \x01(\r\x12\x12\n\nhead_photo\x18\x10 \x01(\r\x12\x1d\n\x15online_battle_win_cnt\x18\x11 \x01(\x05')
  ,
  dependencies=[protocommon_pb2.DESCRIPTOR,rescommon_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CSPKG_CMD_VIEW_PLAYER_INFO_REQ = _descriptor.Descriptor(
  name='CSPKG_CMD_VIEW_PLAYER_INFO_REQ',
  full_name='CSPKG_CMD_VIEW_PLAYER_INFO_REQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='view_role_id', full_name='CSPKG_CMD_VIEW_PLAYER_INFO_REQ.view_role_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vip_level', full_name='CSPKG_CMD_VIEW_PLAYER_INFO_REQ.vip_level', index=1,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_from_gang', full_name='CSPKG_CMD_VIEW_PLAYER_INFO_REQ.is_from_gang', index=2,
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
  serialized_start=56,
  serialized_end=151,
)


_ST_VIEW_PLAYER_HERO_INFO = _descriptor.Descriptor(
  name='ST_VIEW_PlAYER_HERO_INFO',
  full_name='ST_VIEW_PlAYER_HERO_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_id', full_name='ST_VIEW_PlAYER_HERO_INFO.hero_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_lv', full_name='ST_VIEW_PlAYER_HERO_INFO.hero_lv', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_grow_up', full_name='ST_VIEW_PlAYER_HERO_INFO.hero_grow_up', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='emblem_info', full_name='ST_VIEW_PlAYER_HERO_INFO.emblem_info', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equip_info', full_name='ST_VIEW_PlAYER_HERO_INFO.equip_info', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_attr', full_name='ST_VIEW_PlAYER_HERO_INFO.hero_attr', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='talent_info', full_name='ST_VIEW_PlAYER_HERO_INFO.talent_info', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='talent_hide_info', full_name='ST_VIEW_PlAYER_HERO_INFO.talent_hide_info', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='talent_lv_info', full_name='ST_VIEW_PlAYER_HERO_INFO.talent_lv_info', index=8,
      number=9, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equiped_factors', full_name='ST_VIEW_PlAYER_HERO_INFO.equiped_factors', index=9,
      number=10, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='awake_stage', full_name='ST_VIEW_PlAYER_HERO_INFO.awake_stage', index=10,
      number=11, type=13, cpp_type=3, label=1,
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
  serialized_start=154,
  serialized_end=501,
)


_SCPKG_CMD_VIEW_PLAYER_INFO_RES = _descriptor.Descriptor(
  name='SCPKG_CMD_VIEW_PLAYER_INFO_RES',
  full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_from_gang', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.is_from_gang', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='view_role_id', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.view_role_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='view_role_name', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.view_role_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_win_cnt', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.pvp_win_cnt', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_total_cnt', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.pvp_total_cnt', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='greatest_dungeon_id', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.greatest_dungeon_id', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gang_name', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.gang_name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank_battle_pos', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.rank_battle_pos', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='endless_floor', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.endless_floor', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offline_battle_kill', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.offline_battle_kill', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='achievement_rank_pos', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.achievement_rank_pos', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gang_battle_info', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.gang_battle_info', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_info', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.hero_info', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vip_level', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.vip_level', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='head_photo', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.head_photo', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='online_battle_win_cnt', full_name='SCPKG_CMD_VIEW_PLAYER_INFO_RES.online_battle_win_cnt', index=16,
      number=17, type=5, cpp_type=1, label=1,
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
  serialized_start=504,
  serialized_end=989,
)

_ST_VIEW_PLAYER_HERO_INFO.fields_by_name['emblem_info'].message_type = protocommon_pb2._CSDT_EMBLEMINFO_DATA
_ST_VIEW_PLAYER_HERO_INFO.fields_by_name['equip_info'].message_type = rescommon_pb2._CSDT_EQUIPED_INFO
_ST_VIEW_PLAYER_HERO_INFO.fields_by_name['hero_attr'].message_type = rescommon_pb2._HEROATTR
_ST_VIEW_PLAYER_HERO_INFO.fields_by_name['talent_hide_info'].message_type = rescommon_pb2._ST_HERO_BATTLE_TALENT_HIDE_INFO
_SCPKG_CMD_VIEW_PLAYER_INFO_RES.fields_by_name['gang_battle_info'].message_type = protocommon_pb2._CSDT_GANGBATTLE_HERO_INFO
_SCPKG_CMD_VIEW_PLAYER_INFO_RES.fields_by_name['hero_info'].message_type = _ST_VIEW_PLAYER_HERO_INFO
DESCRIPTOR.message_types_by_name['CSPKG_CMD_VIEW_PLAYER_INFO_REQ'] = _CSPKG_CMD_VIEW_PLAYER_INFO_REQ
DESCRIPTOR.message_types_by_name['ST_VIEW_PlAYER_HERO_INFO'] = _ST_VIEW_PLAYER_HERO_INFO
DESCRIPTOR.message_types_by_name['SCPKG_CMD_VIEW_PLAYER_INFO_RES'] = _SCPKG_CMD_VIEW_PLAYER_INFO_RES

CSPKG_CMD_VIEW_PLAYER_INFO_REQ = _reflection.GeneratedProtocolMessageType('CSPKG_CMD_VIEW_PLAYER_INFO_REQ', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_CMD_VIEW_PLAYER_INFO_REQ,
  __module__ = 'viewplayer_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_CMD_VIEW_PLAYER_INFO_REQ)
  ))
_sym_db.RegisterMessage(CSPKG_CMD_VIEW_PLAYER_INFO_REQ)

ST_VIEW_PlAYER_HERO_INFO = _reflection.GeneratedProtocolMessageType('ST_VIEW_PlAYER_HERO_INFO', (_message.Message,), dict(
  DESCRIPTOR = _ST_VIEW_PLAYER_HERO_INFO,
  __module__ = 'viewplayer_pb2'
  # @@protoc_insertion_point(class_scope:ST_VIEW_PlAYER_HERO_INFO)
  ))
_sym_db.RegisterMessage(ST_VIEW_PlAYER_HERO_INFO)

SCPKG_CMD_VIEW_PLAYER_INFO_RES = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_VIEW_PLAYER_INFO_RES', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_VIEW_PLAYER_INFO_RES,
  __module__ = 'viewplayer_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_VIEW_PLAYER_INFO_RES)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_VIEW_PLAYER_INFO_RES)


# @@protoc_insertion_point(module_scope)
