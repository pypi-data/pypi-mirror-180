# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/vpc/v1/address.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/vpc/v1/address.proto',
  package='yandex.cloud.vpc.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!yandex/cloud/vpc/v1/address.proto\x12\x13yandex.cloud.vpc.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xc4\x04\n\x07\x41\x64\x64ress\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x38\n\x06labels\x18\x06 \x03(\x0b\x32(.yandex.cloud.vpc.v1.Address.LabelsEntry\x12I\n\x15\x65xternal_ipv4_address\x18\x07 \x01(\x0b\x32(.yandex.cloud.vpc.v1.ExternalIpv4AddressH\x00\x12\x10\n\x08reserved\x18\x0f \x01(\x08\x12\x0c\n\x04used\x18\x10 \x01(\x08\x12/\n\x04type\x18\x11 \x01(\x0e\x32!.yandex.cloud.vpc.v1.Address.Type\x12:\n\nip_version\x18\x12 \x01(\x0e\x32&.yandex.cloud.vpc.v1.Address.IpVersion\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"8\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08INTERNAL\x10\x01\x12\x0c\n\x08\x45XTERNAL\x10\x02\";\n\tIpVersion\x12\x1a\n\x16IP_VERSION_UNSPECIFIED\x10\x00\x12\x08\n\x04IPV4\x10\x01\x12\x08\n\x04IPV6\x10\x02\x42\x0f\n\x07\x61\x64\x64ress\x12\x04\xc0\xc1\x31\x01\"w\n\x13\x45xternalIpv4Address\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0f\n\x07zone_id\x18\x02 \x01(\t\x12>\n\x0crequirements\x18\x03 \x01(\x0b\x32(.yandex.cloud.vpc.v1.AddressRequirements\"Y\n\x13\x41\x64\x64ressRequirements\x12 \n\x18\x64\x64os_protection_provider\x18\x01 \x01(\t\x12 \n\x18outgoing_smtp_capability\x18\x02 \x01(\tBV\n\x17yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpcb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_ADDRESS_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='yandex.cloud.vpc.v1.Address.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=569,
  serialized_end=625,
)
_sym_db.RegisterEnumDescriptor(_ADDRESS_TYPE)

_ADDRESS_IPVERSION = _descriptor.EnumDescriptor(
  name='IpVersion',
  full_name='yandex.cloud.vpc.v1.Address.IpVersion',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IP_VERSION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IPV4', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IPV6', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=627,
  serialized_end=686,
)
_sym_db.RegisterEnumDescriptor(_ADDRESS_IPVERSION)


_ADDRESS_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.vpc.v1.Address.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.vpc.v1.Address.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.vpc.v1.Address.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=522,
  serialized_end=567,
)

_ADDRESS = _descriptor.Descriptor(
  name='Address',
  full_name='yandex.cloud.vpc.v1.Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.vpc.v1.Address.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.vpc.v1.Address.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.vpc.v1.Address.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.vpc.v1.Address.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.vpc.v1.Address.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.vpc.v1.Address.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='external_ipv4_address', full_name='yandex.cloud.vpc.v1.Address.external_ipv4_address', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reserved', full_name='yandex.cloud.vpc.v1.Address.reserved', index=7,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='used', full_name='yandex.cloud.vpc.v1.Address.used', index=8,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.vpc.v1.Address.type', index=9,
      number=17, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip_version', full_name='yandex.cloud.vpc.v1.Address.ip_version', index=10,
      number=18, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ADDRESS_LABELSENTRY, ],
  enum_types=[
    _ADDRESS_TYPE,
    _ADDRESS_IPVERSION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='address', full_name='yandex.cloud.vpc.v1.Address.address',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\300\3011\001'),
  ],
  serialized_start=123,
  serialized_end=703,
)


_EXTERNALIPV4ADDRESS = _descriptor.Descriptor(
  name='ExternalIpv4Address',
  full_name='yandex.cloud.vpc.v1.ExternalIpv4Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='yandex.cloud.vpc.v1.ExternalIpv4Address.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='zone_id', full_name='yandex.cloud.vpc.v1.ExternalIpv4Address.zone_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requirements', full_name='yandex.cloud.vpc.v1.ExternalIpv4Address.requirements', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=705,
  serialized_end=824,
)


_ADDRESSREQUIREMENTS = _descriptor.Descriptor(
  name='AddressRequirements',
  full_name='yandex.cloud.vpc.v1.AddressRequirements',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ddos_protection_provider', full_name='yandex.cloud.vpc.v1.AddressRequirements.ddos_protection_provider', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outgoing_smtp_capability', full_name='yandex.cloud.vpc.v1.AddressRequirements.outgoing_smtp_capability', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=826,
  serialized_end=915,
)

_ADDRESS_LABELSENTRY.containing_type = _ADDRESS
_ADDRESS.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ADDRESS.fields_by_name['labels'].message_type = _ADDRESS_LABELSENTRY
_ADDRESS.fields_by_name['external_ipv4_address'].message_type = _EXTERNALIPV4ADDRESS
_ADDRESS.fields_by_name['type'].enum_type = _ADDRESS_TYPE
_ADDRESS.fields_by_name['ip_version'].enum_type = _ADDRESS_IPVERSION
_ADDRESS_TYPE.containing_type = _ADDRESS
_ADDRESS_IPVERSION.containing_type = _ADDRESS
_ADDRESS.oneofs_by_name['address'].fields.append(
  _ADDRESS.fields_by_name['external_ipv4_address'])
_ADDRESS.fields_by_name['external_ipv4_address'].containing_oneof = _ADDRESS.oneofs_by_name['address']
_EXTERNALIPV4ADDRESS.fields_by_name['requirements'].message_type = _ADDRESSREQUIREMENTS
DESCRIPTOR.message_types_by_name['Address'] = _ADDRESS
DESCRIPTOR.message_types_by_name['ExternalIpv4Address'] = _EXTERNALIPV4ADDRESS
DESCRIPTOR.message_types_by_name['AddressRequirements'] = _ADDRESSREQUIREMENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ADDRESS_LABELSENTRY,
    '__module__' : 'yandex.cloud.vpc.v1.address_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.Address.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _ADDRESS,
  '__module__' : 'yandex.cloud.vpc.v1.address_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.Address)
  })
_sym_db.RegisterMessage(Address)
_sym_db.RegisterMessage(Address.LabelsEntry)

ExternalIpv4Address = _reflection.GeneratedProtocolMessageType('ExternalIpv4Address', (_message.Message,), {
  'DESCRIPTOR' : _EXTERNALIPV4ADDRESS,
  '__module__' : 'yandex.cloud.vpc.v1.address_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.ExternalIpv4Address)
  })
_sym_db.RegisterMessage(ExternalIpv4Address)

AddressRequirements = _reflection.GeneratedProtocolMessageType('AddressRequirements', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESSREQUIREMENTS,
  '__module__' : 'yandex.cloud.vpc.v1.address_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.AddressRequirements)
  })
_sym_db.RegisterMessage(AddressRequirements)


DESCRIPTOR._options = None
_ADDRESS_LABELSENTRY._options = None
_ADDRESS.oneofs_by_name['address']._options = None
# @@protoc_insertion_point(module_scope)
