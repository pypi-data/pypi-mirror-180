# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iam/v1/api_key_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.iam.v1 import api_key_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_api__key__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/iam/v1/api_key_service.proto',
  package='yandex.cloud.iam.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iam',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)yandex/cloud/iam/v1/api_key_service.proto\x12\x13yandex.cloud.iam.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a!yandex/cloud/iam/v1/api_key.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"4\n\x10GetApiKeyRequest\x12 \n\napi_key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"y\n\x12ListApiKeysRequest\x12$\n\x12service_account_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\"]\n\x13ListApiKeysResponse\x12-\n\x08\x61pi_keys\x18\x01 \x03(\x0b\x32\x1b.yandex.cloud.iam.v1.ApiKey\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"[\n\x13\x43reateApiKeyRequest\x12$\n\x12service_account_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1e\n\x0b\x64\x65scription\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=256\"T\n\x14\x43reateApiKeyResponse\x12,\n\x07\x61pi_key\x18\x01 \x01(\x0b\x32\x1b.yandex.cloud.iam.v1.ApiKey\x12\x0e\n\x06secret\x18\x02 \x01(\t\"\x88\x01\n\x13UpdateApiKeyRequest\x12 \n\napi_key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\"*\n\x14UpdateApiKeyMetadata\x12\x12\n\napi_key_id\x18\x01 \x01(\t\"7\n\x13\x44\x65leteApiKeyRequest\x12 \n\napi_key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"*\n\x14\x44\x65leteApiKeyMetadata\x12\x12\n\napi_key_id\x18\x01 \x01(\t\"~\n\x1bListApiKeyOperationsRequest\x12 \n\napi_key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\"n\n\x1cListApiKeyOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xea\x06\n\rApiKeyService\x12r\n\x04List\x12\'.yandex.cloud.iam.v1.ListApiKeysRequest\x1a(.yandex.cloud.iam.v1.ListApiKeysResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/iam/v1/apiKeys\x12o\n\x03Get\x12%.yandex.cloud.iam.v1.GetApiKeyRequest\x1a\x1b.yandex.cloud.iam.v1.ApiKey\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/iam/v1/apiKeys/{api_key_id}\x12y\n\x06\x43reate\x12(.yandex.cloud.iam.v1.CreateApiKeyRequest\x1a).yandex.cloud.iam.v1.CreateApiKeyResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/iam/v1/apiKeys:\x01*\x12\xa0\x01\n\x06Update\x12(.yandex.cloud.iam.v1.UpdateApiKeyRequest\x1a!.yandex.cloud.operation.Operation\"I\x82\xd3\xe4\x93\x02!2\x1c/iam/v1/apiKeys/{api_key_id}:\x01*\xb2\xd2*\x1e\n\x14UpdateApiKeyMetadata\x12\x06\x41piKey\x12\xac\x01\n\x06\x44\x65lete\x12(.yandex.cloud.iam.v1.DeleteApiKeyRequest\x1a!.yandex.cloud.operation.Operation\"U\x82\xd3\xe4\x93\x02\x1e*\x1c/iam/v1/apiKeys/{api_key_id}\xb2\xd2*-\n\x14\x44\x65leteApiKeyMetadata\x12\x15google.protobuf.Empty\x12\xa6\x01\n\x0eListOperations\x12\x30.yandex.cloud.iam.v1.ListApiKeyOperationsRequest\x1a\x31.yandex.cloud.iam.v1.ListApiKeyOperationsResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/iam/v1/apiKeys/{api_key_id}/operationsBV\n\x17yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iamb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_iam_dot_v1_dot_api__key__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETAPIKEYREQUEST = _descriptor.Descriptor(
  name='GetApiKeyRequest',
  full_name='yandex.cloud.iam.v1.GetApiKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_key_id', full_name='yandex.cloud.iam.v1.GetApiKeyRequest.api_key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=270,
  serialized_end=322,
)


_LISTAPIKEYSREQUEST = _descriptor.Descriptor(
  name='ListApiKeysRequest',
  full_name='yandex.cloud.iam.v1.ListApiKeysRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.iam.v1.ListApiKeysRequest.service_account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.iam.v1.ListApiKeysRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0060-1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.iam.v1.ListApiKeysRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\006<=2000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=324,
  serialized_end=445,
)


_LISTAPIKEYSRESPONSE = _descriptor.Descriptor(
  name='ListApiKeysResponse',
  full_name='yandex.cloud.iam.v1.ListApiKeysResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_keys', full_name='yandex.cloud.iam.v1.ListApiKeysResponse.api_keys', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.iam.v1.ListApiKeysResponse.next_page_token', index=1,
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
  serialized_start=447,
  serialized_end=540,
)


_CREATEAPIKEYREQUEST = _descriptor.Descriptor(
  name='CreateApiKeyRequest',
  full_name='yandex.cloud.iam.v1.CreateApiKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.iam.v1.CreateApiKeyRequest.service_account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.iam.v1.CreateApiKeyRequest.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=256', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=542,
  serialized_end=633,
)


_CREATEAPIKEYRESPONSE = _descriptor.Descriptor(
  name='CreateApiKeyResponse',
  full_name='yandex.cloud.iam.v1.CreateApiKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_key', full_name='yandex.cloud.iam.v1.CreateApiKeyResponse.api_key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret', full_name='yandex.cloud.iam.v1.CreateApiKeyResponse.secret', index=1,
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
  serialized_start=635,
  serialized_end=719,
)


_UPDATEAPIKEYREQUEST = _descriptor.Descriptor(
  name='UpdateApiKeyRequest',
  full_name='yandex.cloud.iam.v1.UpdateApiKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_key_id', full_name='yandex.cloud.iam.v1.UpdateApiKeyRequest.api_key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='yandex.cloud.iam.v1.UpdateApiKeyRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.iam.v1.UpdateApiKeyRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=256', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=722,
  serialized_end=858,
)


_UPDATEAPIKEYMETADATA = _descriptor.Descriptor(
  name='UpdateApiKeyMetadata',
  full_name='yandex.cloud.iam.v1.UpdateApiKeyMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_key_id', full_name='yandex.cloud.iam.v1.UpdateApiKeyMetadata.api_key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=860,
  serialized_end=902,
)


_DELETEAPIKEYREQUEST = _descriptor.Descriptor(
  name='DeleteApiKeyRequest',
  full_name='yandex.cloud.iam.v1.DeleteApiKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_key_id', full_name='yandex.cloud.iam.v1.DeleteApiKeyRequest.api_key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=904,
  serialized_end=959,
)


_DELETEAPIKEYMETADATA = _descriptor.Descriptor(
  name='DeleteApiKeyMetadata',
  full_name='yandex.cloud.iam.v1.DeleteApiKeyMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_key_id', full_name='yandex.cloud.iam.v1.DeleteApiKeyMetadata.api_key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=961,
  serialized_end=1003,
)


_LISTAPIKEYOPERATIONSREQUEST = _descriptor.Descriptor(
  name='ListApiKeyOperationsRequest',
  full_name='yandex.cloud.iam.v1.ListApiKeyOperationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_key_id', full_name='yandex.cloud.iam.v1.ListApiKeyOperationsRequest.api_key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.iam.v1.ListApiKeyOperationsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0060-1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.iam.v1.ListApiKeyOperationsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\006<=2000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1005,
  serialized_end=1131,
)


_LISTAPIKEYOPERATIONSRESPONSE = _descriptor.Descriptor(
  name='ListApiKeyOperationsResponse',
  full_name='yandex.cloud.iam.v1.ListApiKeyOperationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operations', full_name='yandex.cloud.iam.v1.ListApiKeyOperationsResponse.operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.iam.v1.ListApiKeyOperationsResponse.next_page_token', index=1,
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
  serialized_start=1133,
  serialized_end=1243,
)

_LISTAPIKEYSRESPONSE.fields_by_name['api_keys'].message_type = yandex_dot_cloud_dot_iam_dot_v1_dot_api__key__pb2._APIKEY
_CREATEAPIKEYRESPONSE.fields_by_name['api_key'].message_type = yandex_dot_cloud_dot_iam_dot_v1_dot_api__key__pb2._APIKEY
_UPDATEAPIKEYREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_LISTAPIKEYOPERATIONSRESPONSE.fields_by_name['operations'].message_type = yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION
DESCRIPTOR.message_types_by_name['GetApiKeyRequest'] = _GETAPIKEYREQUEST
DESCRIPTOR.message_types_by_name['ListApiKeysRequest'] = _LISTAPIKEYSREQUEST
DESCRIPTOR.message_types_by_name['ListApiKeysResponse'] = _LISTAPIKEYSRESPONSE
DESCRIPTOR.message_types_by_name['CreateApiKeyRequest'] = _CREATEAPIKEYREQUEST
DESCRIPTOR.message_types_by_name['CreateApiKeyResponse'] = _CREATEAPIKEYRESPONSE
DESCRIPTOR.message_types_by_name['UpdateApiKeyRequest'] = _UPDATEAPIKEYREQUEST
DESCRIPTOR.message_types_by_name['UpdateApiKeyMetadata'] = _UPDATEAPIKEYMETADATA
DESCRIPTOR.message_types_by_name['DeleteApiKeyRequest'] = _DELETEAPIKEYREQUEST
DESCRIPTOR.message_types_by_name['DeleteApiKeyMetadata'] = _DELETEAPIKEYMETADATA
DESCRIPTOR.message_types_by_name['ListApiKeyOperationsRequest'] = _LISTAPIKEYOPERATIONSREQUEST
DESCRIPTOR.message_types_by_name['ListApiKeyOperationsResponse'] = _LISTAPIKEYOPERATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetApiKeyRequest = _reflection.GeneratedProtocolMessageType('GetApiKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAPIKEYREQUEST,
  '__module__' : 'yandex.cloud.iam.v1.api_key_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.GetApiKeyRequest)
  })
_sym_db.RegisterMessage(GetApiKeyRequest)

ListApiKeysRequest = _reflection.GeneratedProtocolMessageType('ListApiKeysRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTAPIKEYSREQUEST,
  '__module__' : 'yandex.cloud.iam.v1.api_key_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.ListApiKeysRequest)
  })
_sym_db.RegisterMessage(ListApiKeysRequest)

ListApiKeysResponse = _reflection.GeneratedProtocolMessageType('ListApiKeysResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTAPIKEYSRESPONSE,
  '__module__' : 'yandex.cloud.iam.v1.api_key_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.ListApiKeysResponse)
  })
_sym_db.RegisterMessage(ListApiKeysResponse)

CreateApiKeyRequest = _reflection.GeneratedProtocolMessageType('CreateApiKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEAPIKEYREQUEST,
  '__module__' : 'yandex.cloud.iam.v1.api_key_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.CreateApiKeyRequest)
  })
_sym_db.RegisterMessage(CreateApiKeyRequest)

CreateApiKeyResponse = _reflection.GeneratedProtocolMessageType('CreateApiKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEAPIKEYRESPONSE,
  '__module__' : 'yandex.cloud.iam.v1.api_key_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.CreateApiKeyResponse)
  })
_sym_db.RegisterMessage(CreateApiKeyResponse)

UpdateApiKeyRequest = _reflection.GeneratedProtocolMessageType('UpdateApiKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEAPIKEYREQUEST,
  '__module__' : 'yandex.cloud.iam.v1.api_key_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.UpdateApiKeyRequest)
  })
_sym_db.RegisterMessage(UpdateApiKeyRequest)

UpdateApiKeyMetadata = _reflection.GeneratedProtocolMessageType('UpdateApiKeyMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEAPIKEYMETADATA,
  '__module__' : 'yandex.cloud.iam.v1.api_key_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.UpdateApiKeyMetadata)
  })
_sym_db.RegisterMessage(UpdateApiKeyMetadata)

DeleteApiKeyRequest = _reflection.GeneratedProtocolMessageType('DeleteApiKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEAPIKEYREQUEST,
  '__module__' : 'yandex.cloud.iam.v1.api_key_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.DeleteApiKeyRequest)
  })
_sym_db.RegisterMessage(DeleteApiKeyRequest)

DeleteApiKeyMetadata = _reflection.GeneratedProtocolMessageType('DeleteApiKeyMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEAPIKEYMETADATA,
  '__module__' : 'yandex.cloud.iam.v1.api_key_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.DeleteApiKeyMetadata)
  })
_sym_db.RegisterMessage(DeleteApiKeyMetadata)

ListApiKeyOperationsRequest = _reflection.GeneratedProtocolMessageType('ListApiKeyOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTAPIKEYOPERATIONSREQUEST,
  '__module__' : 'yandex.cloud.iam.v1.api_key_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.ListApiKeyOperationsRequest)
  })
_sym_db.RegisterMessage(ListApiKeyOperationsRequest)

ListApiKeyOperationsResponse = _reflection.GeneratedProtocolMessageType('ListApiKeyOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTAPIKEYOPERATIONSRESPONSE,
  '__module__' : 'yandex.cloud.iam.v1.api_key_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.ListApiKeyOperationsResponse)
  })
_sym_db.RegisterMessage(ListApiKeyOperationsResponse)


DESCRIPTOR._options = None
_GETAPIKEYREQUEST.fields_by_name['api_key_id']._options = None
_LISTAPIKEYSREQUEST.fields_by_name['service_account_id']._options = None
_LISTAPIKEYSREQUEST.fields_by_name['page_size']._options = None
_LISTAPIKEYSREQUEST.fields_by_name['page_token']._options = None
_CREATEAPIKEYREQUEST.fields_by_name['service_account_id']._options = None
_CREATEAPIKEYREQUEST.fields_by_name['description']._options = None
_UPDATEAPIKEYREQUEST.fields_by_name['api_key_id']._options = None
_UPDATEAPIKEYREQUEST.fields_by_name['description']._options = None
_DELETEAPIKEYREQUEST.fields_by_name['api_key_id']._options = None
_LISTAPIKEYOPERATIONSREQUEST.fields_by_name['api_key_id']._options = None
_LISTAPIKEYOPERATIONSREQUEST.fields_by_name['page_size']._options = None
_LISTAPIKEYOPERATIONSREQUEST.fields_by_name['page_token']._options = None

_APIKEYSERVICE = _descriptor.ServiceDescriptor(
  name='ApiKeyService',
  full_name='yandex.cloud.iam.v1.ApiKeyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1246,
  serialized_end=2120,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.iam.v1.ApiKeyService.List',
    index=0,
    containing_service=None,
    input_type=_LISTAPIKEYSREQUEST,
    output_type=_LISTAPIKEYSRESPONSE,
    serialized_options=b'\202\323\344\223\002\021\022\017/iam/v1/apiKeys',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.iam.v1.ApiKeyService.Get',
    index=1,
    containing_service=None,
    input_type=_GETAPIKEYREQUEST,
    output_type=yandex_dot_cloud_dot_iam_dot_v1_dot_api__key__pb2._APIKEY,
    serialized_options=b'\202\323\344\223\002\036\022\034/iam/v1/apiKeys/{api_key_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.iam.v1.ApiKeyService.Create',
    index=2,
    containing_service=None,
    input_type=_CREATEAPIKEYREQUEST,
    output_type=_CREATEAPIKEYRESPONSE,
    serialized_options=b'\202\323\344\223\002\024\"\017/iam/v1/apiKeys:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='yandex.cloud.iam.v1.ApiKeyService.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATEAPIKEYREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002!2\034/iam/v1/apiKeys/{api_key_id}:\001*\262\322*\036\n\024UpdateApiKeyMetadata\022\006ApiKey',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='yandex.cloud.iam.v1.ApiKeyService.Delete',
    index=4,
    containing_service=None,
    input_type=_DELETEAPIKEYREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002\036*\034/iam/v1/apiKeys/{api_key_id}\262\322*-\n\024DeleteApiKeyMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListOperations',
    full_name='yandex.cloud.iam.v1.ApiKeyService.ListOperations',
    index=5,
    containing_service=None,
    input_type=_LISTAPIKEYOPERATIONSREQUEST,
    output_type=_LISTAPIKEYOPERATIONSRESPONSE,
    serialized_options=b'\202\323\344\223\002)\022\'/iam/v1/apiKeys/{api_key_id}/operations',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_APIKEYSERVICE)

DESCRIPTOR.services_by_name['ApiKeyService'] = _APIKEYSERVICE

# @@protoc_insertion_point(module_scope)
