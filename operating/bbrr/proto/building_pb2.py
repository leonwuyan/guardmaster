# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: building.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='building.proto',
  package='',
  serialized_pb=_b('\n\x0e\x62uilding.proto\"u\n\x17\x43SDT_BUILDING_BASE_INFO\x12\x13\n\x0b\x62uilding_id\x18\x01 \x01(\r\x12\x13\n\x0b\x62uilding_lv\x18\x02 \x01(\r\x12\x16\n\x0elevel_beg_time\x18\x03 \x01(\r\x12\x18\n\x10level_total_time\x18\x04 \x01(\r\"k\n\x13\x43SDT_RES_STORE_INFO\x12\x11\n\tres_limit\x18\x01 \x01(\r\x12\x10\n\x08res_type\x18\x02 \x01(\r\x12/\n\rbuilding_info\x18\x03 \x01(\x0b\x32\x18.CSDT_BUILDING_BASE_INFO\"\x85\x01\n\x17\x43SDT_ISLAND_DEFEND_INFO\x12\x0f\n\x07hero_id\x18\x01 \x01(\r\x12\x0f\n\x07hero_lv\x18\x02 \x01(\r\x12\x12\n\nmonster_id\x18\x03 \x01(\r\x12\x12\n\nmonster_lv\x18\x04 \x01(\r\x12\x0f\n\x07trap_id\x18\x05 \x01(\r\x12\x0f\n\x07trap_lv\x18\x06 \x01(\r\"\x9b\x01\n\x14\x43SDT_ISLAND_BORNINFO\x12\x12\n\nborn_speed\x18\x01 \x01(\r\x12\x12\n\nborn_limit\x18\x02 \x01(\r\x12\x16\n\x0elast_born_time\x18\x03 \x01(\r\x12\x14\n\x0c\x63ur_born_res\x18\x04 \x01(\r\x12-\n\x0b\x64\x65\x66\x65nd_info\x18\x05 \x01(\x0b\x32\x18.CSDT_ISLAND_DEFEND_INFO\"\x7f\n\x10\x43SDT_ISLAND_INFO\x12\x10\n\x08res_type\x18\x01 \x01(\r\x12/\n\rbuilding_info\x18\x02 \x03(\x0b\x32\x18.CSDT_BUILDING_BASE_INFO\x12(\n\tborn_info\x18\x03 \x01(\x0b\x32\x15.CSDT_ISLAND_BORNINFO\"z\n\x14\x43SDT_ISLAND_GAININFO\x12\x15\n\rpvp_gain_gold\x18\x01 \x01(\r\x12\x18\n\x10pvp_gain_crystal\x18\x02 \x01(\r\x12\x16\n\x0epvp_gain_money\x18\x03 \x01(\r\x12\x19\n\x11pvp_gain_exp_item\x18\x04 \x01(\r\"\xc9\x01\n\x12\x43SDT_BUILDING_INFO\x12\x31\n\x0fhero_tower_data\x18\x01 \x01(\x0b\x32\x18.CSDT_BUILDING_BASE_INFO\x12,\n\x0eres_store_data\x18\x02 \x03(\x0b\x32\x14.CSDT_RES_STORE_INFO\x12&\n\x0bisland_data\x18\x03 \x03(\x0b\x32\x11.CSDT_ISLAND_INFO\x12*\n\x0bisland_gain\x18\x04 \x01(\x0b\x32\x15.CSDT_ISLAND_GAININFO\"1\n\x1a\x43SPKG_CMD_BUILDING_LEVELUP\x12\x13\n\x0b\x62uilding_id\x18\x01 \x01(\r\"\x8c\x01\n\x1eSCPKG_CMD_BUILDING_LEVELUP_BEG\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x13\n\x0b\x62uilding_id\x18\x02 \x01(\r\x12\x13\n\x0b\x62uilding_lv\x18\x03 \x01(\r\x12\x16\n\x0elevel_beg_time\x18\x04 \x01(\r\x12\x18\n\x10level_total_time\x18\x05 \x01(\r\"Z\n\x1eSCPKG_CMD_BUILDING_LEVELUP_END\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x13\n\x0b\x62uilding_id\x18\x02 \x01(\r\x12\x13\n\x0b\x62uilding_lv\x18\x03 \x01(\r\"E\n\x19SCDT_BUILDING_SIMPLE_INFO\x12\x13\n\x0b\x62uilding_id\x18\x01 \x01(\r\x12\x13\n\x0b\x62uilding_lv\x18\x02 \x01(\r\"^\n\x19SCPKG_CMD_UNLOCK_BUILDING\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x31\n\rbuilding_info\x18\x02 \x03(\x0b\x32\x1a.SCDT_BUILDING_SIMPLE_INFO\":\n#CSPKG_CMD_BUILDING_LEVELUP_DIRECTLY\x12\x13\n\x0b\x62uilding_id\x18\x01 \x01(\r\"B\n\x18SCPKG_CMD_ISLAND_BORNRES\x12\x10\n\x08res_type\x18\x01 \x01(\r\x12\x14\n\x0c\x63ur_born_cnt\x18\x02 \x01(\r\"E\n\x1b\x43SPKG_CMD_SET_ISLAND_DEFEND\x12\x15\n\rbuilding_type\x18\x01 \x01(\r\x12\x0f\n\x07hero_id\x18\x02 \x01(\r\"U\n\x1bSCPKG_CMD_SET_ISLAND_DEFEND\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x15\n\rbuilding_type\x18\x02 \x01(\r\x12\x0f\n\x07hero_id\x18\x03 \x01(\r\"6\n\x1d\x43SPKG_CMD_GET_ISLAND_RESOURCE\x12\x15\n\rbuilding_type\x18\x01 \x01(\r\"I\n\x14SCDT_ISLAND_RESOURCE\x12\x10\n\x08res_type\x18\x01 \x01(\r\x12\x0e\n\x06res_id\x18\x02 \x01(\r\x12\x0f\n\x07res_cnt\x18\x03 \x01(\r\"q\n\x1dSCPKG_CMD_GET_ISLAND_RESOURCE\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x15\n\rbuilding_type\x18\x02 \x01(\r\x12)\n\nobtain_res\x18\x03 \x01(\x0b\x32\x15.SCDT_ISLAND_RESOURCE')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CSDT_BUILDING_BASE_INFO = _descriptor.Descriptor(
  name='CSDT_BUILDING_BASE_INFO',
  full_name='CSDT_BUILDING_BASE_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='building_id', full_name='CSDT_BUILDING_BASE_INFO.building_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building_lv', full_name='CSDT_BUILDING_BASE_INFO.building_lv', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level_beg_time', full_name='CSDT_BUILDING_BASE_INFO.level_beg_time', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level_total_time', full_name='CSDT_BUILDING_BASE_INFO.level_total_time', index=3,
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
  serialized_start=18,
  serialized_end=135,
)


_CSDT_RES_STORE_INFO = _descriptor.Descriptor(
  name='CSDT_RES_STORE_INFO',
  full_name='CSDT_RES_STORE_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res_limit', full_name='CSDT_RES_STORE_INFO.res_limit', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res_type', full_name='CSDT_RES_STORE_INFO.res_type', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building_info', full_name='CSDT_RES_STORE_INFO.building_info', index=2,
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
  serialized_start=137,
  serialized_end=244,
)


_CSDT_ISLAND_DEFEND_INFO = _descriptor.Descriptor(
  name='CSDT_ISLAND_DEFEND_INFO',
  full_name='CSDT_ISLAND_DEFEND_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_id', full_name='CSDT_ISLAND_DEFEND_INFO.hero_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_lv', full_name='CSDT_ISLAND_DEFEND_INFO.hero_lv', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='monster_id', full_name='CSDT_ISLAND_DEFEND_INFO.monster_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='monster_lv', full_name='CSDT_ISLAND_DEFEND_INFO.monster_lv', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trap_id', full_name='CSDT_ISLAND_DEFEND_INFO.trap_id', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trap_lv', full_name='CSDT_ISLAND_DEFEND_INFO.trap_lv', index=5,
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
  serialized_start=247,
  serialized_end=380,
)


_CSDT_ISLAND_BORNINFO = _descriptor.Descriptor(
  name='CSDT_ISLAND_BORNINFO',
  full_name='CSDT_ISLAND_BORNINFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='born_speed', full_name='CSDT_ISLAND_BORNINFO.born_speed', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='born_limit', full_name='CSDT_ISLAND_BORNINFO.born_limit', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_born_time', full_name='CSDT_ISLAND_BORNINFO.last_born_time', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cur_born_res', full_name='CSDT_ISLAND_BORNINFO.cur_born_res', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='defend_info', full_name='CSDT_ISLAND_BORNINFO.defend_info', index=4,
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
  serialized_start=383,
  serialized_end=538,
)


_CSDT_ISLAND_INFO = _descriptor.Descriptor(
  name='CSDT_ISLAND_INFO',
  full_name='CSDT_ISLAND_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res_type', full_name='CSDT_ISLAND_INFO.res_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building_info', full_name='CSDT_ISLAND_INFO.building_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='born_info', full_name='CSDT_ISLAND_INFO.born_info', index=2,
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
  serialized_start=540,
  serialized_end=667,
)


_CSDT_ISLAND_GAININFO = _descriptor.Descriptor(
  name='CSDT_ISLAND_GAININFO',
  full_name='CSDT_ISLAND_GAININFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pvp_gain_gold', full_name='CSDT_ISLAND_GAININFO.pvp_gain_gold', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_gain_crystal', full_name='CSDT_ISLAND_GAININFO.pvp_gain_crystal', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_gain_money', full_name='CSDT_ISLAND_GAININFO.pvp_gain_money', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_gain_exp_item', full_name='CSDT_ISLAND_GAININFO.pvp_gain_exp_item', index=3,
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
  serialized_start=669,
  serialized_end=791,
)


_CSDT_BUILDING_INFO = _descriptor.Descriptor(
  name='CSDT_BUILDING_INFO',
  full_name='CSDT_BUILDING_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_tower_data', full_name='CSDT_BUILDING_INFO.hero_tower_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res_store_data', full_name='CSDT_BUILDING_INFO.res_store_data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='island_data', full_name='CSDT_BUILDING_INFO.island_data', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='island_gain', full_name='CSDT_BUILDING_INFO.island_gain', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=794,
  serialized_end=995,
)


_CSPKG_CMD_BUILDING_LEVELUP = _descriptor.Descriptor(
  name='CSPKG_CMD_BUILDING_LEVELUP',
  full_name='CSPKG_CMD_BUILDING_LEVELUP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='building_id', full_name='CSPKG_CMD_BUILDING_LEVELUP.building_id', index=0,
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
  serialized_start=997,
  serialized_end=1046,
)


_SCPKG_CMD_BUILDING_LEVELUP_BEG = _descriptor.Descriptor(
  name='SCPKG_CMD_BUILDING_LEVELUP_BEG',
  full_name='SCPKG_CMD_BUILDING_LEVELUP_BEG',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SCPKG_CMD_BUILDING_LEVELUP_BEG.result', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building_id', full_name='SCPKG_CMD_BUILDING_LEVELUP_BEG.building_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building_lv', full_name='SCPKG_CMD_BUILDING_LEVELUP_BEG.building_lv', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level_beg_time', full_name='SCPKG_CMD_BUILDING_LEVELUP_BEG.level_beg_time', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level_total_time', full_name='SCPKG_CMD_BUILDING_LEVELUP_BEG.level_total_time', index=4,
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
  serialized_start=1049,
  serialized_end=1189,
)


_SCPKG_CMD_BUILDING_LEVELUP_END = _descriptor.Descriptor(
  name='SCPKG_CMD_BUILDING_LEVELUP_END',
  full_name='SCPKG_CMD_BUILDING_LEVELUP_END',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SCPKG_CMD_BUILDING_LEVELUP_END.result', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building_id', full_name='SCPKG_CMD_BUILDING_LEVELUP_END.building_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building_lv', full_name='SCPKG_CMD_BUILDING_LEVELUP_END.building_lv', index=2,
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
  serialized_start=1191,
  serialized_end=1281,
)


_SCDT_BUILDING_SIMPLE_INFO = _descriptor.Descriptor(
  name='SCDT_BUILDING_SIMPLE_INFO',
  full_name='SCDT_BUILDING_SIMPLE_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='building_id', full_name='SCDT_BUILDING_SIMPLE_INFO.building_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building_lv', full_name='SCDT_BUILDING_SIMPLE_INFO.building_lv', index=1,
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
  serialized_start=1283,
  serialized_end=1352,
)


_SCPKG_CMD_UNLOCK_BUILDING = _descriptor.Descriptor(
  name='SCPKG_CMD_UNLOCK_BUILDING',
  full_name='SCPKG_CMD_UNLOCK_BUILDING',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SCPKG_CMD_UNLOCK_BUILDING.result', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building_info', full_name='SCPKG_CMD_UNLOCK_BUILDING.building_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1354,
  serialized_end=1448,
)


_CSPKG_CMD_BUILDING_LEVELUP_DIRECTLY = _descriptor.Descriptor(
  name='CSPKG_CMD_BUILDING_LEVELUP_DIRECTLY',
  full_name='CSPKG_CMD_BUILDING_LEVELUP_DIRECTLY',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='building_id', full_name='CSPKG_CMD_BUILDING_LEVELUP_DIRECTLY.building_id', index=0,
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
  serialized_start=1450,
  serialized_end=1508,
)


_SCPKG_CMD_ISLAND_BORNRES = _descriptor.Descriptor(
  name='SCPKG_CMD_ISLAND_BORNRES',
  full_name='SCPKG_CMD_ISLAND_BORNRES',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res_type', full_name='SCPKG_CMD_ISLAND_BORNRES.res_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cur_born_cnt', full_name='SCPKG_CMD_ISLAND_BORNRES.cur_born_cnt', index=1,
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
  serialized_start=1510,
  serialized_end=1576,
)


_CSPKG_CMD_SET_ISLAND_DEFEND = _descriptor.Descriptor(
  name='CSPKG_CMD_SET_ISLAND_DEFEND',
  full_name='CSPKG_CMD_SET_ISLAND_DEFEND',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='building_type', full_name='CSPKG_CMD_SET_ISLAND_DEFEND.building_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_id', full_name='CSPKG_CMD_SET_ISLAND_DEFEND.hero_id', index=1,
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
  serialized_start=1578,
  serialized_end=1647,
)


_SCPKG_CMD_SET_ISLAND_DEFEND = _descriptor.Descriptor(
  name='SCPKG_CMD_SET_ISLAND_DEFEND',
  full_name='SCPKG_CMD_SET_ISLAND_DEFEND',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SCPKG_CMD_SET_ISLAND_DEFEND.result', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building_type', full_name='SCPKG_CMD_SET_ISLAND_DEFEND.building_type', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_id', full_name='SCPKG_CMD_SET_ISLAND_DEFEND.hero_id', index=2,
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
  serialized_start=1649,
  serialized_end=1734,
)


_CSPKG_CMD_GET_ISLAND_RESOURCE = _descriptor.Descriptor(
  name='CSPKG_CMD_GET_ISLAND_RESOURCE',
  full_name='CSPKG_CMD_GET_ISLAND_RESOURCE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='building_type', full_name='CSPKG_CMD_GET_ISLAND_RESOURCE.building_type', index=0,
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
  serialized_start=1736,
  serialized_end=1790,
)


_SCDT_ISLAND_RESOURCE = _descriptor.Descriptor(
  name='SCDT_ISLAND_RESOURCE',
  full_name='SCDT_ISLAND_RESOURCE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res_type', full_name='SCDT_ISLAND_RESOURCE.res_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res_id', full_name='SCDT_ISLAND_RESOURCE.res_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res_cnt', full_name='SCDT_ISLAND_RESOURCE.res_cnt', index=2,
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
  serialized_start=1792,
  serialized_end=1865,
)


_SCPKG_CMD_GET_ISLAND_RESOURCE = _descriptor.Descriptor(
  name='SCPKG_CMD_GET_ISLAND_RESOURCE',
  full_name='SCPKG_CMD_GET_ISLAND_RESOURCE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SCPKG_CMD_GET_ISLAND_RESOURCE.result', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building_type', full_name='SCPKG_CMD_GET_ISLAND_RESOURCE.building_type', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='obtain_res', full_name='SCPKG_CMD_GET_ISLAND_RESOURCE.obtain_res', index=2,
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
  serialized_start=1867,
  serialized_end=1980,
)

_CSDT_RES_STORE_INFO.fields_by_name['building_info'].message_type = _CSDT_BUILDING_BASE_INFO
_CSDT_ISLAND_BORNINFO.fields_by_name['defend_info'].message_type = _CSDT_ISLAND_DEFEND_INFO
_CSDT_ISLAND_INFO.fields_by_name['building_info'].message_type = _CSDT_BUILDING_BASE_INFO
_CSDT_ISLAND_INFO.fields_by_name['born_info'].message_type = _CSDT_ISLAND_BORNINFO
_CSDT_BUILDING_INFO.fields_by_name['hero_tower_data'].message_type = _CSDT_BUILDING_BASE_INFO
_CSDT_BUILDING_INFO.fields_by_name['res_store_data'].message_type = _CSDT_RES_STORE_INFO
_CSDT_BUILDING_INFO.fields_by_name['island_data'].message_type = _CSDT_ISLAND_INFO
_CSDT_BUILDING_INFO.fields_by_name['island_gain'].message_type = _CSDT_ISLAND_GAININFO
_SCPKG_CMD_UNLOCK_BUILDING.fields_by_name['building_info'].message_type = _SCDT_BUILDING_SIMPLE_INFO
_SCPKG_CMD_GET_ISLAND_RESOURCE.fields_by_name['obtain_res'].message_type = _SCDT_ISLAND_RESOURCE
DESCRIPTOR.message_types_by_name['CSDT_BUILDING_BASE_INFO'] = _CSDT_BUILDING_BASE_INFO
DESCRIPTOR.message_types_by_name['CSDT_RES_STORE_INFO'] = _CSDT_RES_STORE_INFO
DESCRIPTOR.message_types_by_name['CSDT_ISLAND_DEFEND_INFO'] = _CSDT_ISLAND_DEFEND_INFO
DESCRIPTOR.message_types_by_name['CSDT_ISLAND_BORNINFO'] = _CSDT_ISLAND_BORNINFO
DESCRIPTOR.message_types_by_name['CSDT_ISLAND_INFO'] = _CSDT_ISLAND_INFO
DESCRIPTOR.message_types_by_name['CSDT_ISLAND_GAININFO'] = _CSDT_ISLAND_GAININFO
DESCRIPTOR.message_types_by_name['CSDT_BUILDING_INFO'] = _CSDT_BUILDING_INFO
DESCRIPTOR.message_types_by_name['CSPKG_CMD_BUILDING_LEVELUP'] = _CSPKG_CMD_BUILDING_LEVELUP
DESCRIPTOR.message_types_by_name['SCPKG_CMD_BUILDING_LEVELUP_BEG'] = _SCPKG_CMD_BUILDING_LEVELUP_BEG
DESCRIPTOR.message_types_by_name['SCPKG_CMD_BUILDING_LEVELUP_END'] = _SCPKG_CMD_BUILDING_LEVELUP_END
DESCRIPTOR.message_types_by_name['SCDT_BUILDING_SIMPLE_INFO'] = _SCDT_BUILDING_SIMPLE_INFO
DESCRIPTOR.message_types_by_name['SCPKG_CMD_UNLOCK_BUILDING'] = _SCPKG_CMD_UNLOCK_BUILDING
DESCRIPTOR.message_types_by_name['CSPKG_CMD_BUILDING_LEVELUP_DIRECTLY'] = _CSPKG_CMD_BUILDING_LEVELUP_DIRECTLY
DESCRIPTOR.message_types_by_name['SCPKG_CMD_ISLAND_BORNRES'] = _SCPKG_CMD_ISLAND_BORNRES
DESCRIPTOR.message_types_by_name['CSPKG_CMD_SET_ISLAND_DEFEND'] = _CSPKG_CMD_SET_ISLAND_DEFEND
DESCRIPTOR.message_types_by_name['SCPKG_CMD_SET_ISLAND_DEFEND'] = _SCPKG_CMD_SET_ISLAND_DEFEND
DESCRIPTOR.message_types_by_name['CSPKG_CMD_GET_ISLAND_RESOURCE'] = _CSPKG_CMD_GET_ISLAND_RESOURCE
DESCRIPTOR.message_types_by_name['SCDT_ISLAND_RESOURCE'] = _SCDT_ISLAND_RESOURCE
DESCRIPTOR.message_types_by_name['SCPKG_CMD_GET_ISLAND_RESOURCE'] = _SCPKG_CMD_GET_ISLAND_RESOURCE

CSDT_BUILDING_BASE_INFO = _reflection.GeneratedProtocolMessageType('CSDT_BUILDING_BASE_INFO', (_message.Message,), dict(
  DESCRIPTOR = _CSDT_BUILDING_BASE_INFO,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:CSDT_BUILDING_BASE_INFO)
  ))
_sym_db.RegisterMessage(CSDT_BUILDING_BASE_INFO)

CSDT_RES_STORE_INFO = _reflection.GeneratedProtocolMessageType('CSDT_RES_STORE_INFO', (_message.Message,), dict(
  DESCRIPTOR = _CSDT_RES_STORE_INFO,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:CSDT_RES_STORE_INFO)
  ))
_sym_db.RegisterMessage(CSDT_RES_STORE_INFO)

CSDT_ISLAND_DEFEND_INFO = _reflection.GeneratedProtocolMessageType('CSDT_ISLAND_DEFEND_INFO', (_message.Message,), dict(
  DESCRIPTOR = _CSDT_ISLAND_DEFEND_INFO,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:CSDT_ISLAND_DEFEND_INFO)
  ))
_sym_db.RegisterMessage(CSDT_ISLAND_DEFEND_INFO)

CSDT_ISLAND_BORNINFO = _reflection.GeneratedProtocolMessageType('CSDT_ISLAND_BORNINFO', (_message.Message,), dict(
  DESCRIPTOR = _CSDT_ISLAND_BORNINFO,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:CSDT_ISLAND_BORNINFO)
  ))
_sym_db.RegisterMessage(CSDT_ISLAND_BORNINFO)

CSDT_ISLAND_INFO = _reflection.GeneratedProtocolMessageType('CSDT_ISLAND_INFO', (_message.Message,), dict(
  DESCRIPTOR = _CSDT_ISLAND_INFO,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:CSDT_ISLAND_INFO)
  ))
_sym_db.RegisterMessage(CSDT_ISLAND_INFO)

CSDT_ISLAND_GAININFO = _reflection.GeneratedProtocolMessageType('CSDT_ISLAND_GAININFO', (_message.Message,), dict(
  DESCRIPTOR = _CSDT_ISLAND_GAININFO,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:CSDT_ISLAND_GAININFO)
  ))
_sym_db.RegisterMessage(CSDT_ISLAND_GAININFO)

CSDT_BUILDING_INFO = _reflection.GeneratedProtocolMessageType('CSDT_BUILDING_INFO', (_message.Message,), dict(
  DESCRIPTOR = _CSDT_BUILDING_INFO,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:CSDT_BUILDING_INFO)
  ))
_sym_db.RegisterMessage(CSDT_BUILDING_INFO)

CSPKG_CMD_BUILDING_LEVELUP = _reflection.GeneratedProtocolMessageType('CSPKG_CMD_BUILDING_LEVELUP', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_CMD_BUILDING_LEVELUP,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_CMD_BUILDING_LEVELUP)
  ))
_sym_db.RegisterMessage(CSPKG_CMD_BUILDING_LEVELUP)

SCPKG_CMD_BUILDING_LEVELUP_BEG = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_BUILDING_LEVELUP_BEG', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_BUILDING_LEVELUP_BEG,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_BUILDING_LEVELUP_BEG)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_BUILDING_LEVELUP_BEG)

SCPKG_CMD_BUILDING_LEVELUP_END = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_BUILDING_LEVELUP_END', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_BUILDING_LEVELUP_END,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_BUILDING_LEVELUP_END)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_BUILDING_LEVELUP_END)

SCDT_BUILDING_SIMPLE_INFO = _reflection.GeneratedProtocolMessageType('SCDT_BUILDING_SIMPLE_INFO', (_message.Message,), dict(
  DESCRIPTOR = _SCDT_BUILDING_SIMPLE_INFO,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:SCDT_BUILDING_SIMPLE_INFO)
  ))
_sym_db.RegisterMessage(SCDT_BUILDING_SIMPLE_INFO)

SCPKG_CMD_UNLOCK_BUILDING = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_UNLOCK_BUILDING', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_UNLOCK_BUILDING,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_UNLOCK_BUILDING)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_UNLOCK_BUILDING)

CSPKG_CMD_BUILDING_LEVELUP_DIRECTLY = _reflection.GeneratedProtocolMessageType('CSPKG_CMD_BUILDING_LEVELUP_DIRECTLY', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_CMD_BUILDING_LEVELUP_DIRECTLY,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_CMD_BUILDING_LEVELUP_DIRECTLY)
  ))
_sym_db.RegisterMessage(CSPKG_CMD_BUILDING_LEVELUP_DIRECTLY)

SCPKG_CMD_ISLAND_BORNRES = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_ISLAND_BORNRES', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_ISLAND_BORNRES,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_ISLAND_BORNRES)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_ISLAND_BORNRES)

CSPKG_CMD_SET_ISLAND_DEFEND = _reflection.GeneratedProtocolMessageType('CSPKG_CMD_SET_ISLAND_DEFEND', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_CMD_SET_ISLAND_DEFEND,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_CMD_SET_ISLAND_DEFEND)
  ))
_sym_db.RegisterMessage(CSPKG_CMD_SET_ISLAND_DEFEND)

SCPKG_CMD_SET_ISLAND_DEFEND = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_SET_ISLAND_DEFEND', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_SET_ISLAND_DEFEND,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_SET_ISLAND_DEFEND)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_SET_ISLAND_DEFEND)

CSPKG_CMD_GET_ISLAND_RESOURCE = _reflection.GeneratedProtocolMessageType('CSPKG_CMD_GET_ISLAND_RESOURCE', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_CMD_GET_ISLAND_RESOURCE,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_CMD_GET_ISLAND_RESOURCE)
  ))
_sym_db.RegisterMessage(CSPKG_CMD_GET_ISLAND_RESOURCE)

SCDT_ISLAND_RESOURCE = _reflection.GeneratedProtocolMessageType('SCDT_ISLAND_RESOURCE', (_message.Message,), dict(
  DESCRIPTOR = _SCDT_ISLAND_RESOURCE,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:SCDT_ISLAND_RESOURCE)
  ))
_sym_db.RegisterMessage(SCDT_ISLAND_RESOURCE)

SCPKG_CMD_GET_ISLAND_RESOURCE = _reflection.GeneratedProtocolMessageType('SCPKG_CMD_GET_ISLAND_RESOURCE', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_CMD_GET_ISLAND_RESOURCE,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_CMD_GET_ISLAND_RESOURCE)
  ))
_sym_db.RegisterMessage(SCPKG_CMD_GET_ISLAND_RESOURCE)


# @@protoc_insertion_point(module_scope)
