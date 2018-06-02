# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MemoryGame.proto

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
  name='MemoryGame.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x10MemoryGame.proto\"7\n\x08\x45ndereco\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x10\n\x08\x65ndereco\x18\x02 \x02(\t\x12\r\n\x05porta\x18\x03 \x02(\x05\"\x1b\n\x07\x43onecta\x12\x10\n\x08mensagem\x18\x01 \x02(\t\"\x10\n\x02Id\x12\n\n\x02id\x18\x01 \x02(\x05\x42\x08\n\x06\x65mRede')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ENDERECO = _descriptor.Descriptor(
  name='Endereco',
  full_name='Endereco',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Endereco.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='endereco', full_name='Endereco.endereco', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='porta', full_name='Endereco.porta', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=75,
)


_CONECTA = _descriptor.Descriptor(
  name='Conecta',
  full_name='Conecta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mensagem', full_name='Conecta.mensagem', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=104,
)


_ID = _descriptor.Descriptor(
  name='Id',
  full_name='Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Id.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=122,
)

DESCRIPTOR.message_types_by_name['Endereco'] = _ENDERECO
DESCRIPTOR.message_types_by_name['Conecta'] = _CONECTA
DESCRIPTOR.message_types_by_name['Id'] = _ID

Endereco = _reflection.GeneratedProtocolMessageType('Endereco', (_message.Message,), dict(
  DESCRIPTOR = _ENDERECO,
  __module__ = 'MemoryGame_pb2'
  # @@protoc_insertion_point(class_scope:Endereco)
  ))
_sym_db.RegisterMessage(Endereco)

Conecta = _reflection.GeneratedProtocolMessageType('Conecta', (_message.Message,), dict(
  DESCRIPTOR = _CONECTA,
  __module__ = 'MemoryGame_pb2'
  # @@protoc_insertion_point(class_scope:Conecta)
  ))
_sym_db.RegisterMessage(Conecta)

Id = _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), dict(
  DESCRIPTOR = _ID,
  __module__ = 'MemoryGame_pb2'
  # @@protoc_insertion_point(class_scope:Id)
  ))
_sym_db.RegisterMessage(Id)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\006emRede'))
# @@protoc_insertion_point(module_scope)
