# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/apigateway/websocket/v1/connection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/serverless/apigateway/websocket/v1/connection.proto',
  package='yandex.cloud.serverless.apigateway.websocket.v1',
  syntax='proto3',
  serialized_options=b'\n3yandex.cloud.api.serverless.apigateway.websocket.v1Z]github.com/yandex-cloud/go-genproto/yandex/cloud/serverless/apigateway/websocket/v1;websocket',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n@yandex/cloud/serverless/apigateway/websocket/v1/connection.proto\x12/yandex.cloud.serverless.apigateway.websocket.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xdf\x01\n\nConnection\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ngateway_id\x18\x02 \x01(\t\x12K\n\x08identity\x18\x03 \x01(\x0b\x32\x39.yandex.cloud.serverless.apigateway.websocket.v1.Identity\x12\x30\n\x0c\x63onnected_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0elast_active_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"1\n\x08Identity\x12\x11\n\tsource_ip\x18\x01 \x01(\t\x12\x12\n\nuser_agent\x18\x02 \x01(\tB\x94\x01\n3yandex.cloud.api.serverless.apigateway.websocket.v1Z]github.com/yandex-cloud/go-genproto/yandex/cloud/serverless/apigateway/websocket/v1;websocketb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_CONNECTION = _descriptor.Descriptor(
  name='Connection',
  full_name='yandex.cloud.serverless.apigateway.websocket.v1.Connection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.serverless.apigateway.websocket.v1.Connection.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gateway_id', full_name='yandex.cloud.serverless.apigateway.websocket.v1.Connection.gateway_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identity', full_name='yandex.cloud.serverless.apigateway.websocket.v1.Connection.identity', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connected_at', full_name='yandex.cloud.serverless.apigateway.websocket.v1.Connection.connected_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_active_at', full_name='yandex.cloud.serverless.apigateway.websocket.v1.Connection.last_active_at', index=4,
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
  serialized_start=151,
  serialized_end=374,
)


_IDENTITY = _descriptor.Descriptor(
  name='Identity',
  full_name='yandex.cloud.serverless.apigateway.websocket.v1.Identity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_ip', full_name='yandex.cloud.serverless.apigateway.websocket.v1.Identity.source_ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_agent', full_name='yandex.cloud.serverless.apigateway.websocket.v1.Identity.user_agent', index=1,
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
  serialized_start=376,
  serialized_end=425,
)

_CONNECTION.fields_by_name['identity'].message_type = _IDENTITY
_CONNECTION.fields_by_name['connected_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CONNECTION.fields_by_name['last_active_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Connection'] = _CONNECTION
DESCRIPTOR.message_types_by_name['Identity'] = _IDENTITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Connection = _reflection.GeneratedProtocolMessageType('Connection', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTION,
  '__module__' : 'yandex.cloud.serverless.apigateway.websocket.v1.connection_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.apigateway.websocket.v1.Connection)
  })
_sym_db.RegisterMessage(Connection)

Identity = _reflection.GeneratedProtocolMessageType('Identity', (_message.Message,), {
  'DESCRIPTOR' : _IDENTITY,
  '__module__' : 'yandex.cloud.serverless.apigateway.websocket.v1.connection_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.apigateway.websocket.v1.Identity)
  })
_sym_db.RegisterMessage(Identity)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
