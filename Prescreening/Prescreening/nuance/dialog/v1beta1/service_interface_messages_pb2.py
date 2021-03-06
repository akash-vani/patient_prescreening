# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nuance/dialog/v1beta1/service-interface-messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from Prescreening.nuance.dialog.v1beta1 import runtime_interface_messages_pb2 as nuance_dot_dialog_dot_v1beta1_dot_runtime__interface__messages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nuance/dialog/v1beta1/service-interface-messages.proto',
  package='nuance.dialog.channelconnector.v1beta1',
  syntax='proto3',
  serialized_options=_b('\n?com.nuance.coretech.dialog.channelconnector.v1.service.messagesP\001'),
  serialized_pb=_b('\n6nuance/dialog/v1beta1/service-interface-messages.proto\x12&nuance.dialog.channelconnector.v1beta1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x36nuance/dialog/v1beta1/runtime-interface-messages.proto\"\xb0\x01\n\x0cStartRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12@\n\x08selector\x18\x02 \x01(\x0b\x32..nuance.dialog.runtime.common.v1beta1.Selector\x12J\n\x07payload\x18\x03 \x01(\x0b\x32\x39.nuance.dialog.runtime.common.v1beta1.StartRequestPayload\"\\\n\rStartResponse\x12K\n\x07payload\x18\x01 \x01(\x0b\x32:.nuance.dialog.runtime.common.v1beta1.StartResponsePayload\"\xb4\x01\n\x0e\x45xecuteRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12@\n\x08selector\x18\x02 \x01(\x0b\x32..nuance.dialog.runtime.common.v1beta1.Selector\x12L\n\x07payload\x18\x03 \x01(\x0b\x32;.nuance.dialog.runtime.common.v1beta1.ExecuteRequestPayload\"`\n\x0f\x45xecuteResponse\x12M\n\x07payload\x18\x01 \x01(\x0b\x32<.nuance.dialog.runtime.common.v1beta1.ExecuteResponsePayload\"!\n\x0bStopRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\"\x0e\n\x0cStopResponseBC\n?com.nuance.coretech.dialog.channelconnector.v1.service.messagesP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,nuance_dot_dialog_dot_v1beta1_dot_runtime__interface__messages__pb2.DESCRIPTOR,])




_STARTREQUEST = _descriptor.Descriptor(
  name='StartRequest',
  full_name='nuance.dialog.channelconnector.v1beta1.StartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='nuance.dialog.channelconnector.v1beta1.StartRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selector', full_name='nuance.dialog.channelconnector.v1beta1.StartRequest.selector', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='nuance.dialog.channelconnector.v1beta1.StartRequest.payload', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=185,
  serialized_end=361,
)


_STARTRESPONSE = _descriptor.Descriptor(
  name='StartResponse',
  full_name='nuance.dialog.channelconnector.v1beta1.StartResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='nuance.dialog.channelconnector.v1beta1.StartResponse.payload', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_end=455,
)


_EXECUTEREQUEST = _descriptor.Descriptor(
  name='ExecuteRequest',
  full_name='nuance.dialog.channelconnector.v1beta1.ExecuteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='nuance.dialog.channelconnector.v1beta1.ExecuteRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selector', full_name='nuance.dialog.channelconnector.v1beta1.ExecuteRequest.selector', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='nuance.dialog.channelconnector.v1beta1.ExecuteRequest.payload', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=458,
  serialized_end=638,
)


_EXECUTERESPONSE = _descriptor.Descriptor(
  name='ExecuteResponse',
  full_name='nuance.dialog.channelconnector.v1beta1.ExecuteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='nuance.dialog.channelconnector.v1beta1.ExecuteResponse.payload', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=640,
  serialized_end=736,
)


_STOPREQUEST = _descriptor.Descriptor(
  name='StopRequest',
  full_name='nuance.dialog.channelconnector.v1beta1.StopRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='nuance.dialog.channelconnector.v1beta1.StopRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=738,
  serialized_end=771,
)


_STOPRESPONSE = _descriptor.Descriptor(
  name='StopResponse',
  full_name='nuance.dialog.channelconnector.v1beta1.StopResponse',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=773,
  serialized_end=787,
)

_STARTREQUEST.fields_by_name['selector'].message_type = nuance_dot_dialog_dot_v1beta1_dot_runtime__interface__messages__pb2._SELECTOR
_STARTREQUEST.fields_by_name['payload'].message_type = nuance_dot_dialog_dot_v1beta1_dot_runtime__interface__messages__pb2._STARTREQUESTPAYLOAD
_STARTRESPONSE.fields_by_name['payload'].message_type = nuance_dot_dialog_dot_v1beta1_dot_runtime__interface__messages__pb2._STARTRESPONSEPAYLOAD
_EXECUTEREQUEST.fields_by_name['selector'].message_type = nuance_dot_dialog_dot_v1beta1_dot_runtime__interface__messages__pb2._SELECTOR
_EXECUTEREQUEST.fields_by_name['payload'].message_type = nuance_dot_dialog_dot_v1beta1_dot_runtime__interface__messages__pb2._EXECUTEREQUESTPAYLOAD
_EXECUTERESPONSE.fields_by_name['payload'].message_type = nuance_dot_dialog_dot_v1beta1_dot_runtime__interface__messages__pb2._EXECUTERESPONSEPAYLOAD
DESCRIPTOR.message_types_by_name['StartRequest'] = _STARTREQUEST
DESCRIPTOR.message_types_by_name['StartResponse'] = _STARTRESPONSE
DESCRIPTOR.message_types_by_name['ExecuteRequest'] = _EXECUTEREQUEST
DESCRIPTOR.message_types_by_name['ExecuteResponse'] = _EXECUTERESPONSE
DESCRIPTOR.message_types_by_name['StopRequest'] = _STOPREQUEST
DESCRIPTOR.message_types_by_name['StopResponse'] = _STOPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StartRequest = _reflection.GeneratedProtocolMessageType('StartRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTREQUEST,
  '__module__' : 'nuance.dialog.v1beta1.service_interface_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dialog.channelconnector.v1beta1.StartRequest)
  })
_sym_db.RegisterMessage(StartRequest)

StartResponse = _reflection.GeneratedProtocolMessageType('StartResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTRESPONSE,
  '__module__' : 'nuance.dialog.v1beta1.service_interface_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dialog.channelconnector.v1beta1.StartResponse)
  })
_sym_db.RegisterMessage(StartResponse)

ExecuteRequest = _reflection.GeneratedProtocolMessageType('ExecuteRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEREQUEST,
  '__module__' : 'nuance.dialog.v1beta1.service_interface_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dialog.channelconnector.v1beta1.ExecuteRequest)
  })
_sym_db.RegisterMessage(ExecuteRequest)

ExecuteResponse = _reflection.GeneratedProtocolMessageType('ExecuteResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTERESPONSE,
  '__module__' : 'nuance.dialog.v1beta1.service_interface_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dialog.channelconnector.v1beta1.ExecuteResponse)
  })
_sym_db.RegisterMessage(ExecuteResponse)

StopRequest = _reflection.GeneratedProtocolMessageType('StopRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPREQUEST,
  '__module__' : 'nuance.dialog.v1beta1.service_interface_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dialog.channelconnector.v1beta1.StopRequest)
  })
_sym_db.RegisterMessage(StopRequest)

StopResponse = _reflection.GeneratedProtocolMessageType('StopResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOPRESPONSE,
  '__module__' : 'nuance.dialog.v1beta1.service_interface_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dialog.channelconnector.v1beta1.StopResponse)
  })
_sym_db.RegisterMessage(StopResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
