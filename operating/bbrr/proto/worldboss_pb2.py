# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: worldboss.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='worldboss.proto',
  package='',
  serialized_pb=_b('\n\x0fworldboss.proto\x1a\x11protocommon.proto\"U\n&SCPKG_CMD_PLAYER_DUNBALANCE_WORLD_BOSS\x12\x13\n\x0breward_gold\x18\x01 \x01(\r\x12\x16\n\x0ereward_crystal\x18\x02 \x01(\r\".\n\x1aSCPKG_CMD_WORLD_BOSS_ERROR\x12\x10\n\x08\x65rror_no\x18\x01 \x01(\r\"M\n\'SCPKG_CMD_PLAYER_WORLD_BOSS_KILL_REWARD\x12\"\n\tdrop_info\x18\x01 \x01(\x0b\x32\x0f.CSDT_DROP_INFO\"X\n\'SCPKG_CMD_WORLD_BOSS_DAMAGE_RANK_PLAYER\x12\x0b\n\x03uid\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\ndamage_sum\x18\x03 \x01(\r\"k\n\x1cSCPKG_WORLD_BOSS_KILLER_INFO\x12\r\n\x05index\x18\x01 \x01(\r\x12\x0b\n\x03uid\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\tvip_level\x18\x04 \x01(\r\x12\x0e\n\x06\x64\x61mage\x18\x05 \x01(\r\"C\n CSPKG_WORLD_BOSS_KILLER_INFO_REQ\x12\x0b\n\x03uid\x18\x01 \x01(\r\x12\x12\n\nboss_index\x18\x02 \x01(\r\"0\n\x1f\x43SPKG_CMD_WORLD_BOSS_STATUS_REQ\x12\r\n\x05param\x18\x01 \x01(\r\"5\n$CSPKG_CMD_WORLD_BOSS_CHANGE_HERO_REQ\x12\r\n\x05param\x18\x01 \x01(\r\"F\n$SCPKG_CMD_WORLD_BOSS_CHANGE_HERO_RES\x12\r\n\x05param\x18\x01 \x01(\r\x12\x0f\n\x07hero_id\x18\x02 \x01(\r\"o\n\x14\x43SDT_WORLD_BOSS_HERO\x12\x0f\n\x07hero_id\x18\x01 \x01(\r\x12\x1e\n\x16hero_remain_hp_percent\x18\x02 \x01(\r\x12\x16\n\x0eremain_seconds\x18\x03 \x01(\r\x12\x0e\n\x06\x64\x61mage\x18\x04 \x01(\r\"~\n#SCPKG_CMD_WORLD_BOSS_CHALLENGE_DATA\x12\x18\n\x10world_boss_index\x18\x01 \x01(\r\x12\x12\n\nhero_index\x18\x02 \x01(\r\x12)\n\nhero_array\x18\x03 \x03(\x0b\x32\x15.CSDT_WORLD_BOSS_HERO\"\xf6\x01\n\x1bSCPKG_CMD_WORLD_BOSS_STATUS\x12\x16\n\x0e\x63ur_boss_index\x18\x01 \x01(\r\x12\x13\n\x0b\x63ur_boss_id\x18\x02 \x01(\r\x12\x17\n\x0f\x63ur_boss_max_hp\x18\x03 \x01(\x04\x12\x17\n\x0f\x63ur_boss_cur_hp\x18\x04 \x01(\x04\x12 \n\x18\x63ur_boss_refresh_seconds\x18\x05 \x01(\r\x12\x10\n\x08week_day\x18\x06 \x01(\r\x12!\n\x19sync_interval_sec_in_menu\x18\x08 \x01(\r\x12!\n\x19sync_interval_sec_in_game\x18\x07 \x01(\r\"j\n\x1b\x43SPKG_CMD_UPDATE_WORLD_BOSS\x12\x12\n\nboss_index\x18\x01 \x01(\r\x12\x17\n\x0f\x62oss_got_damage\x18\x02 \x01(\r\x12\x1e\n\x16hero_hp_remain_percent\x18\x03 \x01(\r\"i\n\x1bSCPKG_CMD_UPDATE_WORLD_BOSS\x12\x0f\n\x07\x62oss_hp\x18\x01 \x01(\x04\x12\x1d\n\x15killer_player_role_id\x18\x02 \x01(\r\x12\x1a\n\x12killer_player_name\x18\x03 \x01(\t\"X\n\x19SCPKG_CMD_WORLD_BOSS_DEAD\x12\x12\n\nboss_index\x18\x01 \x01(\r\x12\x12\n\nkiller_uid\x18\x02 \x01(\r\x12\x13\n\x0bkiller_name\x18\x03 \x01(\t')
  ,
  dependencies=[protocommon_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SCPKG_CMD_PLAYER_DUNBALANCE_WORLD_BOSS = _descriptor.Descriptor(
  name='SCPKG_CMD_PLAYER_DUNBALANCE_WORLD_BOSS',
  full_name='SCPKG_CMD_PLAYER_DUNBALANCE_WORLD_BOSS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reward_gold', full_name='SCPKG_CMD_PLAYER_DUNBALANCE_WORLD_BOSS.reward_gold', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward_crystal', full_name='SCPKG_CMD_PLAYER_DUNBALANCE_WORLD_BOSS.reward_crystal', index=1,
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
  serialized_start=38,
  serialized_end=123,
)


_SCPKG_CMD_WORLD_BOSS_ERROR = _descriptor.Descriptor(
  name='SCPKG_CMD_WORLD_BOSS_ERROR',
  full_name='SCPKG_CMD_WORLD_BOSS_ERROR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_no', full_name='SCPKG_CMD_WORLD_BOSS_ERROR.error_no', index=0,
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
  serialized_start=125,
  serialized_end=171,
)


_SCPKG_CMD_PLAYER_WORLD_BOSS_KILL_REWARD = _descriptor.Descriptor(
  name='SCPKG_CMD_PLAYER_WORLD_BOSS_KILL_REWARD',
  full_name='SCPKG_CMD_PLAYER_WORLD_BOSS_KILL_REWARD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='drop_info', full_name='SCPKG_CMD_PLAYER_WORLD_BOSS_KILL_REWARD.drop_info', index=0,
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
  serialized_start=173,
  serialized_end=250,
)


_SCPKG_CMD_WORLD_BOSS_DAMAGE_RANK_PLAYER = _descriptor.Descriptor(
  name='SCPKG_CMD_WORLD_BOSS_DAMAGE_RANK_PLAYER',
  full_name='SCPKG_CMD_WORLD_BOSS_DAMAGE_RANK_PLAYER',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='SCPKG_CMD_WORLD_BOSS_DAMAGE_RANK_PLAYER.uid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='SCPKG_CMD_WORLD_BOSS_DAMAGE_RANK_PLAYER.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='damage_sum', full_name='SCPKG_CMD_WORLD_BOSS_DAMAGE_RANK_PLAYER.damage_sum', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=252,
  serialized_end=340,
)


_SCPKG_WORLD_BOSS_KILLER_INFO = _descriptor.Descriptor(
  name='SCPKG_WORLD_BOSS_KILLER_INFO',
  full_name='SCPKG_WORLD_BOSS_KILLER_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='SCPKG_WORLD_BOSS_KILLER_INFO.index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='SCPKG_WORLD_BOSS_KILLER_INFO.uid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='SCPKG_WORLD_BOSS_KILLER_INFO.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vip_level', full_name='SCPKG_WORLD_BOSS_KILLER_INFO.vip_level', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='damage', full_name='SCPKG_WORLD_BOSS_KILLER_INFO.damage', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=342,
  serialized_end=449,
)


_CSPKG_WORLD_BOSS_KILLER_INFO_REQ = _descriptor.Descriptor(
  name='CSPKG_WORLD_BOSS_KILLER_INFO_REQ',
  full_name='CSPKG_WORLD_BOSS_KILLER_INFO_REQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='CSPKG_WORLD_BOSS_KILLER_INFO_REQ.uid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boss_index', full_name='CSPKG_WORLD_BOSS_KILLER_INFO_REQ.boss_index', index=1,
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
  serialized_start=451,
  serialized_end=518,
)


_CSPKG_CMD_WORLD_BOSS_STATUS_REQ = _descriptor.Descriptor(
  name='CSPKG_CMD_WORLD_BOSS_STATUS_REQ',
  full_name='CSPKG_CMD_WORLD_BOSS_STATUS_REQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param', full_name='CSPKG_CMD_WORLD_BOSS_STATUS_REQ.param', index=0,
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
  serialized_start=520,
  serialized_end=568,
)


_CSPKG_CMD_WORLD_BOSS_CHANGE_HERO_REQ = _descriptor.Descriptor(
  name='CSPKG_CMD_WORLD_BOSS_CHANGE_HERO_REQ',
  full_name='CSPKG_CMD_WORLD_BOSS_CHANGE_HERO_REQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param', full_name='CSPKG_CMD_WORLD_BOSS_CHANGE_HERO_REQ.param', index=0,
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
  serialized_start=570,
  serialized_end=623,
)


_SCPKG_CMD_WORLD_BOSS_CHANGE_HERO_RES = _descriptor.Descriptor(
  name='SCPKG_CMD_WORLD_BOSS_CHANGE_HERO_RES',
  full_name='SCPKG_CMD_WORLD_BOSS_CHANGE_HERO_RES',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param', full_name='SCPKG_CMD_WORLD_BOSS_CHANGE_HERO_RES.param', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_id', full_name='SCPKG_CMD_WORLD_BOSS_CHANGE_HERO_RES.hero_id', index=1,
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
  serialized_start=625,
  serialized_end=695,
)


_CSDT_WORLD_BOSS_HERO = _descriptor.Descriptor(
  name='CSDT_WORLD_BOSS_HERO',
  full_name='CSDT_WORLD_BOSS_HERO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_id', full_name='CSDT_WORLD_BOSS_HERO.hero_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_remain_hp_percent', full_name='CSDT_WORLD_BOSS_HERO.hero_remain_hp_percent', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remain_seconds', full_name='CSDT_WORLD_BOSS_HERO.remain_seconds', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='damage', full_name='CSDT_WORLD_BOSS_HERO.damage', index=3,
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
  serialized_start=697,
  serialized_end=808,
)


_SCPKG_CMD_WORLD_BOSS_CHALLENGE_DATA = _descriptor.Descriptor(
  name='SCPKG_CMD_WORLD_BOSS_CHALLENGE_DATA',
  full_name='SCPKG_CMD_WORLD_BOSS_CHALLENGE_DATA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='world_boss_index', full_name='SCPKG_CMD_WORLD_BOSS_CHALLENGE_DATA.world_boss_index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_index', full_name='SCPKG_CMD_WORLD_BOSS_CHALLENGE_DATA.hero_index', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_array', full_name='SCPKG_CMD_WORLD_BOSS_CHALLENGE_DATA.hero_array', index=2,
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
  serialized_start=810,
  serialized_end=936,
)


_SCPKG_CMD_WORLD_BOSS_STATUS = _descriptor.Descriptor(
  name='SCPKG_CMD_WORLD_BOSS_STATUS',
  full_name='SCPKG_CMD_WORLD_BOSS_STATUS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cur_boss_index', full_name='SCPKG_CMD_WORLD_BOSS_STATUS.cur_boss_index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cur_boss_id', full_name='SCPKG_CMD_WORLD_BOSS_STATUS.cur_boss_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cur_boss_max_hp', full_name='SCPKG_CMD_WORLD_BOSS_STATUS.cur_boss_max_hp', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cur_boss_cur_hp', full_name='SCPKG_CMD_WORLD_BOSS_STATUS.cur_boss_cur_hp', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cur_boss_refresh_seconds', full_name='SCPKG_CMD_WORLD_BOSS_STATUS.cur_boss_refresh_seconds', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='week_day', full_name='SCPKG_CMD_WORLD_BOSS_STATUS.week_day', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sync_interval_sec_in_menu', full_name='SCPKG_CMD_WORLD_BOSS_STATUS.sync_interval_sec_in_menu', index=6,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sync_interval_sec_in_game', full_name='SCPKG_CMD_WORLD_BOSS_STATUS.sync_interval_sec_in_game', index=7,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=939,
  serialized_end=1185,
)


_CSPKG_CMD_UPDATE_WORLD_BOSS = _descriptor.Descriptor(
  name='CSPKG_CMD_UPDATE_WORLD_BOSS',
  full_name='CSPKG_CMD_UPDATE_WORLD_BOSS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boss_index', full_name='CSPKG_CMD_UPDATE_WORLD_BOSS.boss_index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boss_got_damage', full_name='CSPKG_CMD_UPDATE_WORLD_BOSS.boss_got_damage', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_hp_remain_percent', full_name='CSPKG_CMD_UPDATE_WORLD_BOSS.hero_hp_remain_percent', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=1187,
  serialized_end=1293,
)


_SCPKG_CMD_UPDATE_WORLD_BOSS = _descriptor.Descriptor(
  name='SCPKG_CMD_UPDATE_WORLD_BOSS',
  full_name='SCPKG_CMD_UPDATE_WORLD_BOSS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boss_hp', full_name='SCPKG_CMD_UPDATE_WORLD_BOSS.boss_hp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='killer_player_role_id', full_name='SCPKG_CMD_UPDATE_WORLD_BOSS.killer_player_role_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='killer_player_name', full_name='SCPKG_CMD_UPDATE_WORLD_BOSS.killer_player_name', index=2,
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
  serialized_start=1295,
  serialized_end=1400,
)


_SCPKG_CMD_WORLD_BOSS_DEAD = _descriptor.Descriptor(
  name='SCPKG_CMD_WORLD_BOSS_DEAD',
  full_name='SCPKG_CMD_WORLD_BOSS_DEAD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boss_index', full_name='SCPKG_CMD_WORLD_BOSS_DEAD.boss_index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='killer_uid', full_name='SCPKG_CMD_WORLD_BOSS_DEAD.killer_uid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='killer_name', full_name='SCPKG_CMD_WORLD_BOSS_DEAD.killer_name', index=2,
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
  serialized_start=1402,
  serialized_end=1490,
)

_SCPKG_CMD_PLAYER_WORLD_BOSS_KILL_REWARD.fields_by_name['drop_info'].message_type = protocommon_pb2._CSDT_DROP_INFO
_SCPKG_CMD_WORLD_BOSS_CHALLENGE_DATA.fields_by_name['hero_array'].message_type = _CSDT_WORLD_BOSS_HERO
DESCRIPTOR.message_types_by_name['SCPKG_CMD_PLAYER_DUNBALANCE_WORLD_BOSS'] = _SCPKG_CMD_PLAYER_DUNBALANCE_WORLD_BOSS
DESCRIPTOR.message_types_by_name['SCPKG_CMD_WORLD_BOSS_ERROR'] = _SCPKG_CMD_WORLD_BOSS_ERROR
DESCRIPTOR.message_types_by_name['SCPKG_CMD_PLAYER_WORLD_BOSS_KILL_REWARD'] = _SCPKG_CMD_PLAYER_WORLD_BOSS_KILL_REWARD
DESCRIPTOR.message_types_by_name['SCPKG_CMD_WORLD_BOSS_DAMAGE_RANK_PLAYER'] = _SCPKG_CMD_WORLD_BOSS_DAMAGE_RANK_PLAYER
DESCRIPTOR.message_types_by_name['SCPKG_WORLD_BOSS_KILLER_INFO'] = _SCPKG_WORLD_BOSS_KILLER_INFO
DESCRIPTOR.message_types_by_name['CSPKG_WORLD_BOSS_KILLER_INFO_REQ'] = _CSPKG_WORLD_BOSS_KILLER_INFO_REQ
DESCRIPTOR.message_types_by_name['CSPKG_CMD_WORLD_BOSS_STATUS_REQ'] = _CSPKG_CMD_WORLD_BOSS_STATUS_REQ
DESCRIPTOR.message_types_by_name['CSPKG_CMD_WORLD_BOSS_CHANGE_HERO_REQ'] = _CSPKG_CMD_WORLD_BOSS_CHANGE_HERO_REQ
DESCRIPTOR.message_types_by_name['SCPKG_CMD_WORLD_BOSS_CHANGE_HERO_RES'] = _SCPKG_CMD_WORLD_BOSS_CHANGE_HERO_RES
DESCRIPTOR.message_types_by_name['CSDT_WORLD_BOSS_HERO'] = _CSDT_WORLD_BOSS_HERO
DESCRIPTOR.message_types_by_name['SCPKG_CMD_WORLD_BOSS_CHALLENGE_DATA'] = _SCPKG_CMD_WORLD_BOSS_CHALLENGE_DATA
DESCRIPTOR.message_types_by_name['SCPKG_CMD_WORLD_BOSS_STATUS'] = _SCPKG_CMD_WORLD_BOSS_STATUS
DESCRIPTOR.message_types_by_name['CSPKG_CMD_UPDATE_WORLD_BOSS'] = _CSPKG_CMD_UPDATE_WORLD_BOSS
DESCRIPTOR.message_types_by_name['SCPKG_CMD_UPDATE_WORLD_BOSS'] = _SCPKG_CMD_UPDATE_WORLD_BOSS
DESCRIPTOR.message_types_by_name['SCPKG_CMD_WORLD_BOSS_DEAD'] = _SCPKG_CMD_WORLD_BOSS_DEAD

SCPKG_CMD_PLAYER_DUNBALANCE_WORLD_BOSS = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_PLAYER_DUNBALANCE_WORLD_BOSS', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_PLAYER_DUNBALANCE_WORLD_BOSS,
  __module__ = 'worldboss_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_PLAYER_DUNBALANCE_WORLD_BOSS)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_PLAYER_DUNBALANCE_WORLD_BOSS)

SCPKG_CMD_WORLD_BOSS_ERROR = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_WORLD_BOSS_ERROR', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_WORLD_BOSS_ERROR,
  __module__ = 'worldboss_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_WORLD_BOSS_ERROR)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_WORLD_BOSS_ERROR)

SCPKG_CMD_PLAYER_WORLD_BOSS_KILL_REWARD = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_PLAYER_WORLD_BOSS_KILL_REWARD', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_PLAYER_WORLD_BOSS_KILL_REWARD,
  __module__ = 'worldboss_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_PLAYER_WORLD_BOSS_KILL_REWARD)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_PLAYER_WORLD_BOSS_KILL_REWARD)

SCPKG_CMD_WORLD_BOSS_DAMAGE_RANK_PLAYER = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_WORLD_BOSS_DAMAGE_RANK_PLAYER', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_WORLD_BOSS_DAMAGE_RANK_PLAYER,
  __module__ = 'worldboss_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_WORLD_BOSS_DAMAGE_RANK_PLAYER)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_WORLD_BOSS_DAMAGE_RANK_PLAYER)

SCPKG_WORLD_BOSS_KILLER_INFO = _reflection.GeneratedProtocolMessageType('SCPKG_WORLD_BOSS_KILLER_INFO', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_WORLD_BOSS_KILLER_INFO,
  __module__ = 'worldboss_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_WORLD_BOSS_KILLER_INFO)
  ))
_sym_db.RegisterMessage(SCPKG_WORLD_BOSS_KILLER_INFO)

CSPKG_WORLD_BOSS_KILLER_INFO_REQ = _reflection.GeneratedProtocolMessageType('CSPKG_WORLD_BOSS_KILLER_INFO_REQ', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_WORLD_BOSS_KILLER_INFO_REQ,
  __module__ = 'worldboss_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_WORLD_BOSS_KILLER_INFO_REQ)
  ))
_sym_db.RegisterMessage(CSPKG_WORLD_BOSS_KILLER_INFO_REQ)

CSPKG_CMD_WORLD_BOSS_STATUS_REQ = _reflection.GeneratedProtocolMessageType('CSPKG_CMD_WORLD_BOSS_STATUS_REQ', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_CMD_WORLD_BOSS_STATUS_REQ,
  __module__ = 'worldboss_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_CMD_WORLD_BOSS_STATUS_REQ)
  ))
_sym_db.RegisterMessage(CSPKG_CMD_WORLD_BOSS_STATUS_REQ)

CSPKG_CMD_WORLD_BOSS_CHANGE_HERO_REQ = _reflection.GeneratedProtocolMessageType('CSPKG_CMD_WORLD_BOSS_CHANGE_HERO_REQ', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_CMD_WORLD_BOSS_CHANGE_HERO_REQ,
  __module__ = 'worldboss_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_CMD_WORLD_BOSS_CHANGE_HERO_REQ)
  ))
_sym_db.RegisterMessage(CSPKG_CMD_WORLD_BOSS_CHANGE_HERO_REQ)

SCPKG_CMD_WORLD_BOSS_CHANGE_HERO_RES = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_WORLD_BOSS_CHANGE_HERO_RES', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_WORLD_BOSS_CHANGE_HERO_RES,
  __module__ = 'worldboss_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_WORLD_BOSS_CHANGE_HERO_RES)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_WORLD_BOSS_CHANGE_HERO_RES)

CSDT_WORLD_BOSS_HERO = _reflection.GeneratedProtocolMessageType('CSDT_WORLD_BOSS_HERO', (_message.Message,), dict(
  DESCRIPTOR = _CSDT_WORLD_BOSS_HERO,
  __module__ = 'worldboss_pb2'
  # @@protoc_insertion_point(class_scope:CSDT_WORLD_BOSS_HERO)
  ))
_sym_db.RegisterMessage(CSDT_WORLD_BOSS_HERO)

SCPKG_CMD_WORLD_BOSS_CHALLENGE_DATA = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_WORLD_BOSS_CHALLENGE_DATA', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_WORLD_BOSS_CHALLENGE_DATA,
  __module__ = 'worldboss_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_WORLD_BOSS_CHALLENGE_DATA)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_WORLD_BOSS_CHALLENGE_DATA)

SCPKG_CMD_WORLD_BOSS_STATUS = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_WORLD_BOSS_STATUS', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_WORLD_BOSS_STATUS,
  __module__ = 'worldboss_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_WORLD_BOSS_STATUS)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_WORLD_BOSS_STATUS)

CSPKG_CMD_UPDATE_WORLD_BOSS = _reflection.GeneratedProtocolMessageType('CSPKG_CMD_UPDATE_WORLD_BOSS', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_CMD_UPDATE_WORLD_BOSS,
  __module__ = 'worldboss_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_CMD_UPDATE_WORLD_BOSS)
  ))
_sym_db.RegisterMessage(CSPKG_CMD_UPDATE_WORLD_BOSS)

SCPKG_CMD_UPDATE_WORLD_BOSS = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_UPDATE_WORLD_BOSS', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_UPDATE_WORLD_BOSS,
  __module__ = 'worldboss_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_UPDATE_WORLD_BOSS)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_UPDATE_WORLD_BOSS)

SCPKG_CMD_WORLD_BOSS_DEAD = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_WORLD_BOSS_DEAD', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_WORLD_BOSS_DEAD,
  __module__ = 'worldboss_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_WORLD_BOSS_DEAD)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_WORLD_BOSS_DEAD)


# @@protoc_insertion_point(module_scope)
