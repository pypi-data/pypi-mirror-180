# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/organizationmanager/v1/user_account.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/organizationmanager/v1/user_account.proto',
  package='yandex.cloud.organizationmanager.v1',
  syntax='proto3',
  serialized_options=b'\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanager',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6yandex/cloud/organizationmanager/v1/user_account.proto\x12#yandex.cloud.organizationmanager.v1\x1a\x1dyandex/cloud/validation.proto\"\xea\x01\n\x0bUserAccount\x12\n\n\x02id\x18\x01 \x01(\t\x12\x66\n\x1cyandex_passport_user_account\x18\x02 \x01(\x0b\x32>.yandex.cloud.organizationmanager.v1.YandexPassportUserAccountH\x00\x12Q\n\x11saml_user_account\x18\x03 \x01(\x0b\x32\x34.yandex.cloud.organizationmanager.v1.SamlUserAccountH\x00\x42\x14\n\x0cuser_account\x12\x04\xc0\xc1\x31\x01\"A\n\x19YandexPassportUserAccount\x12\r\n\x05login\x18\x01 \x01(\t\x12\x15\n\rdefault_email\x18\x02 \x01(\t\"\xbf\x02\n\x0fSamlUserAccount\x12#\n\rfederation_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1e\n\x07name_id\x18\x02 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05\x31-256\x12X\n\nattributes\x18\x03 \x03(\x0b\x32\x44.yandex.cloud.organizationmanager.v1.SamlUserAccount.AttributesEntry\x1a\x1a\n\tAttribute\x12\r\n\x05value\x18\x01 \x03(\t\x1aq\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12M\n\x05value\x18\x02 \x01(\x0b\x32>.yandex.cloud.organizationmanager.v1.SamlUserAccount.Attribute:\x02\x38\x01\x42\x86\x01\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanagerb\x06proto3'
  ,
  dependencies=[yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_USERACCOUNT = _descriptor.Descriptor(
  name='UserAccount',
  full_name='yandex.cloud.organizationmanager.v1.UserAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.organizationmanager.v1.UserAccount.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yandex_passport_user_account', full_name='yandex.cloud.organizationmanager.v1.UserAccount.yandex_passport_user_account', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='saml_user_account', full_name='yandex.cloud.organizationmanager.v1.UserAccount.saml_user_account', index=2,
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
    _descriptor.OneofDescriptor(
      name='user_account', full_name='yandex.cloud.organizationmanager.v1.UserAccount.user_account',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\300\3011\001'),
  ],
  serialized_start=127,
  serialized_end=361,
)


_YANDEXPASSPORTUSERACCOUNT = _descriptor.Descriptor(
  name='YandexPassportUserAccount',
  full_name='yandex.cloud.organizationmanager.v1.YandexPassportUserAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='yandex.cloud.organizationmanager.v1.YandexPassportUserAccount.login', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_email', full_name='yandex.cloud.organizationmanager.v1.YandexPassportUserAccount.default_email', index=1,
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
  serialized_start=363,
  serialized_end=428,
)


_SAMLUSERACCOUNT_ATTRIBUTE = _descriptor.Descriptor(
  name='Attribute',
  full_name='yandex.cloud.organizationmanager.v1.SamlUserAccount.Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.organizationmanager.v1.SamlUserAccount.Attribute.value', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=609,
  serialized_end=635,
)

_SAMLUSERACCOUNT_ATTRIBUTESENTRY = _descriptor.Descriptor(
  name='AttributesEntry',
  full_name='yandex.cloud.organizationmanager.v1.SamlUserAccount.AttributesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.organizationmanager.v1.SamlUserAccount.AttributesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.organizationmanager.v1.SamlUserAccount.AttributesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=637,
  serialized_end=750,
)

_SAMLUSERACCOUNT = _descriptor.Descriptor(
  name='SamlUserAccount',
  full_name='yandex.cloud.organizationmanager.v1.SamlUserAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='federation_id', full_name='yandex.cloud.organizationmanager.v1.SamlUserAccount.federation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name_id', full_name='yandex.cloud.organizationmanager.v1.SamlUserAccount.name_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\0051-256', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='yandex.cloud.organizationmanager.v1.SamlUserAccount.attributes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SAMLUSERACCOUNT_ATTRIBUTE, _SAMLUSERACCOUNT_ATTRIBUTESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=431,
  serialized_end=750,
)

_USERACCOUNT.fields_by_name['yandex_passport_user_account'].message_type = _YANDEXPASSPORTUSERACCOUNT
_USERACCOUNT.fields_by_name['saml_user_account'].message_type = _SAMLUSERACCOUNT
_USERACCOUNT.oneofs_by_name['user_account'].fields.append(
  _USERACCOUNT.fields_by_name['yandex_passport_user_account'])
_USERACCOUNT.fields_by_name['yandex_passport_user_account'].containing_oneof = _USERACCOUNT.oneofs_by_name['user_account']
_USERACCOUNT.oneofs_by_name['user_account'].fields.append(
  _USERACCOUNT.fields_by_name['saml_user_account'])
_USERACCOUNT.fields_by_name['saml_user_account'].containing_oneof = _USERACCOUNT.oneofs_by_name['user_account']
_SAMLUSERACCOUNT_ATTRIBUTE.containing_type = _SAMLUSERACCOUNT
_SAMLUSERACCOUNT_ATTRIBUTESENTRY.fields_by_name['value'].message_type = _SAMLUSERACCOUNT_ATTRIBUTE
_SAMLUSERACCOUNT_ATTRIBUTESENTRY.containing_type = _SAMLUSERACCOUNT
_SAMLUSERACCOUNT.fields_by_name['attributes'].message_type = _SAMLUSERACCOUNT_ATTRIBUTESENTRY
DESCRIPTOR.message_types_by_name['UserAccount'] = _USERACCOUNT
DESCRIPTOR.message_types_by_name['YandexPassportUserAccount'] = _YANDEXPASSPORTUSERACCOUNT
DESCRIPTOR.message_types_by_name['SamlUserAccount'] = _SAMLUSERACCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserAccount = _reflection.GeneratedProtocolMessageType('UserAccount', (_message.Message,), {
  'DESCRIPTOR' : _USERACCOUNT,
  '__module__' : 'yandex.cloud.organizationmanager.v1.user_account_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.UserAccount)
  })
_sym_db.RegisterMessage(UserAccount)

YandexPassportUserAccount = _reflection.GeneratedProtocolMessageType('YandexPassportUserAccount', (_message.Message,), {
  'DESCRIPTOR' : _YANDEXPASSPORTUSERACCOUNT,
  '__module__' : 'yandex.cloud.organizationmanager.v1.user_account_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.YandexPassportUserAccount)
  })
_sym_db.RegisterMessage(YandexPassportUserAccount)

SamlUserAccount = _reflection.GeneratedProtocolMessageType('SamlUserAccount', (_message.Message,), {

  'Attribute' : _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), {
    'DESCRIPTOR' : _SAMLUSERACCOUNT_ATTRIBUTE,
    '__module__' : 'yandex.cloud.organizationmanager.v1.user_account_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.SamlUserAccount.Attribute)
    })
  ,

  'AttributesEntry' : _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), {
    'DESCRIPTOR' : _SAMLUSERACCOUNT_ATTRIBUTESENTRY,
    '__module__' : 'yandex.cloud.organizationmanager.v1.user_account_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.SamlUserAccount.AttributesEntry)
    })
  ,
  'DESCRIPTOR' : _SAMLUSERACCOUNT,
  '__module__' : 'yandex.cloud.organizationmanager.v1.user_account_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.SamlUserAccount)
  })
_sym_db.RegisterMessage(SamlUserAccount)
_sym_db.RegisterMessage(SamlUserAccount.Attribute)
_sym_db.RegisterMessage(SamlUserAccount.AttributesEntry)


DESCRIPTOR._options = None
_USERACCOUNT.oneofs_by_name['user_account']._options = None
_SAMLUSERACCOUNT_ATTRIBUTESENTRY._options = None
_SAMLUSERACCOUNT.fields_by_name['federation_id']._options = None
_SAMLUSERACCOUNT.fields_by_name['name_id']._options = None
# @@protoc_insertion_point(module_scope)
