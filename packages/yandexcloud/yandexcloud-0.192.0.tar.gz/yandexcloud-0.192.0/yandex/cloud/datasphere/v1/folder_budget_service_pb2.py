# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datasphere/v1/folder_budget_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/datasphere/v1/folder_budget_service.proto',
  package='yandex.cloud.datasphere.v1',
  syntax='proto3',
  serialized_options=b'\n\036yandex.cloud.api.datasphere.v1ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v1;datasphere',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6yandex/cloud/datasphere/v1/folder_budget_service.proto\x12\x1ayandex.cloud.datasphere.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"9\n\x16GetFolderBudgetRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\xc3\x01\n\x17GetFolderBudgetResponse\x12\x31\n\x0cunit_balance\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x37\n\x12max_units_per_hour\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12<\n\x17max_units_per_execution\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\x91\x02\n\x16SetFolderBudgetRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12,\n\x08set_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x31\n\x0cunit_balance\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x37\n\x12max_units_per_hour\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12<\n\x17max_units_per_execution\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value2\xc3\x02\n\x13\x46olderBudgetService\x12\xa1\x01\n\x03Get\x12\x32.yandex.cloud.datasphere.v1.GetFolderBudgetRequest\x1a\x33.yandex.cloud.datasphere.v1.GetFolderBudgetResponse\"1\x82\xd3\xe4\x93\x02+\x12)/datasphere/v1/folders/{folder_id}:budget\x12\x87\x01\n\x03Set\x12\x32.yandex.cloud.datasphere.v1.SetFolderBudgetRequest\x1a\x16.google.protobuf.Empty\"4\x82\xd3\xe4\x93\x02.\")/datasphere/v1/folders/{folder_id}:budget:\x01*Bk\n\x1eyandex.cloud.api.datasphere.v1ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v1;datasphereb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETFOLDERBUDGETREQUEST = _descriptor.Descriptor(
  name='GetFolderBudgetRequest',
  full_name='yandex.cloud.datasphere.v1.GetFolderBudgetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.datasphere.v1.GetFolderBudgetRequest.folder_id', index=0,
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
  serialized_start=242,
  serialized_end=299,
)


_GETFOLDERBUDGETRESPONSE = _descriptor.Descriptor(
  name='GetFolderBudgetResponse',
  full_name='yandex.cloud.datasphere.v1.GetFolderBudgetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='unit_balance', full_name='yandex.cloud.datasphere.v1.GetFolderBudgetResponse.unit_balance', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_units_per_hour', full_name='yandex.cloud.datasphere.v1.GetFolderBudgetResponse.max_units_per_hour', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_units_per_execution', full_name='yandex.cloud.datasphere.v1.GetFolderBudgetResponse.max_units_per_execution', index=2,
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
  serialized_start=302,
  serialized_end=497,
)


_SETFOLDERBUDGETREQUEST = _descriptor.Descriptor(
  name='SetFolderBudgetRequest',
  full_name='yandex.cloud.datasphere.v1.SetFolderBudgetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.datasphere.v1.SetFolderBudgetRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='set_mask', full_name='yandex.cloud.datasphere.v1.SetFolderBudgetRequest.set_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unit_balance', full_name='yandex.cloud.datasphere.v1.SetFolderBudgetRequest.unit_balance', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_units_per_hour', full_name='yandex.cloud.datasphere.v1.SetFolderBudgetRequest.max_units_per_hour', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_units_per_execution', full_name='yandex.cloud.datasphere.v1.SetFolderBudgetRequest.max_units_per_execution', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=500,
  serialized_end=773,
)

_GETFOLDERBUDGETRESPONSE.fields_by_name['unit_balance'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_GETFOLDERBUDGETRESPONSE.fields_by_name['max_units_per_hour'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_GETFOLDERBUDGETRESPONSE.fields_by_name['max_units_per_execution'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SETFOLDERBUDGETREQUEST.fields_by_name['set_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_SETFOLDERBUDGETREQUEST.fields_by_name['unit_balance'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SETFOLDERBUDGETREQUEST.fields_by_name['max_units_per_hour'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SETFOLDERBUDGETREQUEST.fields_by_name['max_units_per_execution'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['GetFolderBudgetRequest'] = _GETFOLDERBUDGETREQUEST
DESCRIPTOR.message_types_by_name['GetFolderBudgetResponse'] = _GETFOLDERBUDGETRESPONSE
DESCRIPTOR.message_types_by_name['SetFolderBudgetRequest'] = _SETFOLDERBUDGETREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFolderBudgetRequest = _reflection.GeneratedProtocolMessageType('GetFolderBudgetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFOLDERBUDGETREQUEST,
  '__module__' : 'yandex.cloud.datasphere.v1.folder_budget_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datasphere.v1.GetFolderBudgetRequest)
  })
_sym_db.RegisterMessage(GetFolderBudgetRequest)

GetFolderBudgetResponse = _reflection.GeneratedProtocolMessageType('GetFolderBudgetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFOLDERBUDGETRESPONSE,
  '__module__' : 'yandex.cloud.datasphere.v1.folder_budget_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datasphere.v1.GetFolderBudgetResponse)
  })
_sym_db.RegisterMessage(GetFolderBudgetResponse)

SetFolderBudgetRequest = _reflection.GeneratedProtocolMessageType('SetFolderBudgetRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETFOLDERBUDGETREQUEST,
  '__module__' : 'yandex.cloud.datasphere.v1.folder_budget_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datasphere.v1.SetFolderBudgetRequest)
  })
_sym_db.RegisterMessage(SetFolderBudgetRequest)


DESCRIPTOR._options = None
_GETFOLDERBUDGETREQUEST.fields_by_name['folder_id']._options = None
_SETFOLDERBUDGETREQUEST.fields_by_name['folder_id']._options = None

_FOLDERBUDGETSERVICE = _descriptor.ServiceDescriptor(
  name='FolderBudgetService',
  full_name='yandex.cloud.datasphere.v1.FolderBudgetService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=776,
  serialized_end=1099,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.datasphere.v1.FolderBudgetService.Get',
    index=0,
    containing_service=None,
    input_type=_GETFOLDERBUDGETREQUEST,
    output_type=_GETFOLDERBUDGETRESPONSE,
    serialized_options=b'\202\323\344\223\002+\022)/datasphere/v1/folders/{folder_id}:budget',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Set',
    full_name='yandex.cloud.datasphere.v1.FolderBudgetService.Set',
    index=1,
    containing_service=None,
    input_type=_SETFOLDERBUDGETREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002.\")/datasphere/v1/folders/{folder_id}:budget:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FOLDERBUDGETSERVICE)

DESCRIPTOR.services_by_name['FolderBudgetService'] = _FOLDERBUDGETSERVICE

# @@protoc_insertion_point(module_scope)
