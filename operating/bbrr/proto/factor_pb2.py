# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: factor.proto

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
  name='factor.proto',
  package='',
  serialized_pb=_b('\n\x0c\x66\x61\x63tor.proto\";\n\x17SCDT_NOTIFY_FACTOR_DATA\x12\x11\n\tfactor_id\x18\x01 \x02(\r\x12\r\n\x05\x63ount\x18\x02 \x02(\r\"O\n\x17SCPKG_NTF_FACTOR_CHANGE\x12\x0c\n\x04type\x18\x01 \x02(\r\x12&\n\x04info\x18\x02 \x03(\x0b\x32\x18.SCDT_NOTIFY_FACTOR_DATA\"\xb5\x01\n\x1cSCDT_NOTIFY_HERO_FACTOR_DATA\x12\x0f\n\x07hero_id\x18\x01 \x02(\r\x12\x18\n\x10\x66\x61\x63tor_slot_info\x18\x02 \x03(\r\x12\x17\n\x0f\x66\x61\x63tor_skill_id\x18\x03 \x02(\r\x12\x16\n\x0e\x66\x61\x63tor_attr_id\x18\x04 \x03(\r\x12\x1a\n\x12\x66\x61\x63tor_skill_ratio\x18\x05 \x01(\r\x12\x1d\n\x15\x66\x61\x63tor_skill_cooldown\x18\x06 \x01(\r\"D\n\x15SCPKG_NTF_HERO_FACTOR\x12+\n\x04info\x18\x01 \x03(\x0b\x32\x1d.SCDT_NOTIFY_HERO_FACTOR_DATA\"B\n\x1b\x43SPKG_REMOVE_EMBEDED_FACTOR\x12\x0f\n\x07hero_id\x18\x01 \x02(\r\x12\x12\n\nslot_index\x18\x02 \x02(\r\"8\n\x12\x43SPKG_EMBED_FACTOR\x12\x0f\n\x07hero_id\x18\x01 \x02(\r\x12\x11\n\tfactor_id\x18\x02 \x02(\r\"3\n CSPKG_REMOVE_ALL_EMBEDED_FACTORS\x12\x0f\n\x07hero_id\x18\x01 \x02(\r\"\x1b\n\x19\x43SPKG_UPGRADE_ALL_FACTORS\"9\n\x14\x43SPKG_UPGRADE_FACTOR\x12\x11\n\tfactor_id\x18\x01 \x02(\r\x12\x0e\n\x06\x61mount\x18\x02 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SCDT_NOTIFY_FACTOR_DATA = _descriptor.Descriptor(
  name='SCDT_NOTIFY_FACTOR_DATA',
  full_name='SCDT_NOTIFY_FACTOR_DATA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='factor_id', full_name='SCDT_NOTIFY_FACTOR_DATA.factor_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='SCDT_NOTIFY_FACTOR_DATA.count', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=16,
  serialized_end=75,
)


_SCPKG_NTF_FACTOR_CHANGE = _descriptor.Descriptor(
  name='SCPKG_NTF_FACTOR_CHANGE',
  full_name='SCPKG_NTF_FACTOR_CHANGE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='SCPKG_NTF_FACTOR_CHANGE.type', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='SCPKG_NTF_FACTOR_CHANGE.info', index=1,
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
  serialized_start=77,
  serialized_end=156,
)


_SCDT_NOTIFY_HERO_FACTOR_DATA = _descriptor.Descriptor(
  name='SCDT_NOTIFY_HERO_FACTOR_DATA',
  full_name='SCDT_NOTIFY_HERO_FACTOR_DATA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_id', full_name='SCDT_NOTIFY_HERO_FACTOR_DATA.hero_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='factor_slot_info', full_name='SCDT_NOTIFY_HERO_FACTOR_DATA.factor_slot_info', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='factor_skill_id', full_name='SCDT_NOTIFY_HERO_FACTOR_DATA.factor_skill_id', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='factor_attr_id', full_name='SCDT_NOTIFY_HERO_FACTOR_DATA.factor_attr_id', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='factor_skill_ratio', full_name='SCDT_NOTIFY_HERO_FACTOR_DATA.factor_skill_ratio', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='factor_skill_cooldown', full_name='SCDT_NOTIFY_HERO_FACTOR_DATA.factor_skill_cooldown', index=5,
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
  serialized_start=159,
  serialized_end=340,
)


_SCPKG_NTF_HERO_FACTOR = _descriptor.Descriptor(
  name='SCPKG_NTF_HERO_FACTOR',
  full_name='SCPKG_NTF_HERO_FACTOR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='SCPKG_NTF_HERO_FACTOR.info', index=0,
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
  serialized_start=342,
  serialized_end=410,
)


_CSPKG_REMOVE_EMBEDED_FACTOR = _descriptor.Descriptor(
  name='CSPKG_REMOVE_EMBEDED_FACTOR',
  full_name='CSPKG_REMOVE_EMBEDED_FACTOR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_id', full_name='CSPKG_REMOVE_EMBEDED_FACTOR.hero_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_index', full_name='CSPKG_REMOVE_EMBEDED_FACTOR.slot_index', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=412,
  serialized_end=478,
)


_CSPKG_EMBED_FACTOR = _descriptor.Descriptor(
  name='CSPKG_EMBED_FACTOR',
  full_name='CSPKG_EMBED_FACTOR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_id', full_name='CSPKG_EMBED_FACTOR.hero_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='factor_id', full_name='CSPKG_EMBED_FACTOR.factor_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=480,
  serialized_end=536,
)


_CSPKG_REMOVE_ALL_EMBEDED_FACTORS = _descriptor.Descriptor(
  name='CSPKG_REMOVE_ALL_EMBEDED_FACTORS',
  full_name='CSPKG_REMOVE_ALL_EMBEDED_FACTORS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_id', full_name='CSPKG_REMOVE_ALL_EMBEDED_FACTORS.hero_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
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
  serialized_start=538,
  serialized_end=589,
)


_CSPKG_UPGRADE_ALL_FACTORS = _descriptor.Descriptor(
  name='CSPKG_UPGRADE_ALL_FACTORS',
  full_name='CSPKG_UPGRADE_ALL_FACTORS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=591,
  serialized_end=618,
)


_CSPKG_UPGRADE_FACTOR = _descriptor.Descriptor(
  name='CSPKG_UPGRADE_FACTOR',
  full_name='CSPKG_UPGRADE_FACTOR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='factor_id', full_name='CSPKG_UPGRADE_FACTOR.factor_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='CSPKG_UPGRADE_FACTOR.amount', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=620,
  serialized_end=677,
)

_SCPKG_NTF_FACTOR_CHANGE.fields_by_name['info'].message_type = _SCDT_NOTIFY_FACTOR_DATA
_SCPKG_NTF_HERO_FACTOR.fields_by_name['info'].message_type = _SCDT_NOTIFY_HERO_FACTOR_DATA
DESCRIPTOR.message_types_by_name['SCDT_NOTIFY_FACTOR_DATA'] = _SCDT_NOTIFY_FACTOR_DATA
DESCRIPTOR.message_types_by_name['SCPKG_NTF_FACTOR_CHANGE'] = _SCPKG_NTF_FACTOR_CHANGE
DESCRIPTOR.message_types_by_name['SCDT_NOTIFY_HERO_FACTOR_DATA'] = _SCDT_NOTIFY_HERO_FACTOR_DATA
DESCRIPTOR.message_types_by_name['SCPKG_NTF_HERO_FACTOR'] = _SCPKG_NTF_HERO_FACTOR
DESCRIPTOR.message_types_by_name['CSPKG_REMOVE_EMBEDED_FACTOR'] = _CSPKG_REMOVE_EMBEDED_FACTOR
DESCRIPTOR.message_types_by_name['CSPKG_EMBED_FACTOR'] = _CSPKG_EMBED_FACTOR
DESCRIPTOR.message_types_by_name['CSPKG_REMOVE_ALL_EMBEDED_FACTORS'] = _CSPKG_REMOVE_ALL_EMBEDED_FACTORS
DESCRIPTOR.message_types_by_name['CSPKG_UPGRADE_ALL_FACTORS'] = _CSPKG_UPGRADE_ALL_FACTORS
DESCRIPTOR.message_types_by_name['CSPKG_UPGRADE_FACTOR'] = _CSPKG_UPGRADE_FACTOR

SCDT_NOTIFY_FACTOR_DATA = _reflection.GeneratedProtocolMessageType('SCDT_NOTIFY_FACTOR_DATA', (_message.Message,), dict(
  DESCRIPTOR = _SCDT_NOTIFY_FACTOR_DATA,
  __module__ = 'factor_pb2'
  # @@protoc_insertion_point(class_scope:SCDT_NOTIFY_FACTOR_DATA)
  ))
_sym_db.RegisterMessage(SCDT_NOTIFY_FACTOR_DATA)

SCPKG_NTF_FACTOR_CHANGE = _reflection.GeneratedProtocolMessageType('SCPKG_NTF_FACTOR_CHANGE', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_NTF_FACTOR_CHANGE,
  __module__ = 'factor_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_NTF_FACTOR_CHANGE)
  ))
_sym_db.RegisterMessage(SCPKG_NTF_FACTOR_CHANGE)

SCDT_NOTIFY_HERO_FACTOR_DATA = _reflection.GeneratedProtocolMessageType('SCDT_NOTIFY_HERO_FACTOR_DATA', (_message.Message,), dict(
  DESCRIPTOR = _SCDT_NOTIFY_HERO_FACTOR_DATA,
  __module__ = 'factor_pb2'
  # @@protoc_insertion_point(class_scope:SCDT_NOTIFY_HERO_FACTOR_DATA)
  ))
_sym_db.RegisterMessage(SCDT_NOTIFY_HERO_FACTOR_DATA)

SCPKG_NTF_HERO_FACTOR = _reflection.GeneratedProtocolMessageType('SCPKG_NTF_HERO_FACTOR', (_message.Message,), dict(
  DESCRIPTOR = _SCPKG_NTF_HERO_FACTOR,
  __module__ = 'factor_pb2'
  # @@protoc_insertion_point(class_scope:SCPKG_NTF_HERO_FACTOR)
  ))
_sym_db.RegisterMessage(SCPKG_NTF_HERO_FACTOR)

CSPKG_REMOVE_EMBEDED_FACTOR = _reflection.GeneratedProtocolMessageType('CSPKG_REMOVE_EMBEDED_FACTOR', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_REMOVE_EMBEDED_FACTOR,
  __module__ = 'factor_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_REMOVE_EMBEDED_FACTOR)
  ))
_sym_db.RegisterMessage(CSPKG_REMOVE_EMBEDED_FACTOR)

CSPKG_EMBED_FACTOR = _reflection.GeneratedProtocolMessageType('CSPKG_EMBED_FACTOR', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_EMBED_FACTOR,
  __module__ = 'factor_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_EMBED_FACTOR)
  ))
_sym_db.RegisterMessage(CSPKG_EMBED_FACTOR)

CSPKG_REMOVE_ALL_EMBEDED_FACTORS = _reflection.GeneratedProtocolMessageType('CSPKG_REMOVE_ALL_EMBEDED_FACTORS', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_REMOVE_ALL_EMBEDED_FACTORS,
  __module__ = 'factor_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_REMOVE_ALL_EMBEDED_FACTORS)
  ))
_sym_db.RegisterMessage(CSPKG_REMOVE_ALL_EMBEDED_FACTORS)

CSPKG_UPGRADE_ALL_FACTORS = _reflection.GeneratedProtocolMessageType('CSPKG_UPGRADE_ALL_FACTORS', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_UPGRADE_ALL_FACTORS,
  __module__ = 'factor_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_UPGRADE_ALL_FACTORS)
  ))
_sym_db.RegisterMessage(CSPKG_UPGRADE_ALL_FACTORS)

CSPKG_UPGRADE_FACTOR = _reflection.GeneratedProtocolMessageType('CSPKG_UPGRADE_FACTOR', (_message.Message,), dict(
  DESCRIPTOR = _CSPKG_UPGRADE_FACTOR,
  __module__ = 'factor_pb2'
  # @@protoc_insertion_point(class_scope:CSPKG_UPGRADE_FACTOR)
  ))
_sym_db.RegisterMessage(CSPKG_UPGRADE_FACTOR)


# @@protoc_insertion_point(module_scope)
