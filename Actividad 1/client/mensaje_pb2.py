# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mensaje.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mensaje.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rmensaje.proto\"I\n\x0fMessage_request\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\t\x12\x0f\n\x07id_dest\x18\x04 \x01(\x05\"6\n\rMessage_reply\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\t\"\x14\n\x06\x43lient\x12\n\n\x02id\x18\x01 \x01(\x05\"\x06\n\x04Null2r\n\x06Sender\x12\x32\n\x0csend_message\x12\x10.Message_request\x1a\x0e.Message_reply\"\x00\x12\x34\n\x0erecept_message\x12\x10.Message_request\x1a\x0e.Message_reply\"\x00\x32\x34\n\x0c\x43lients_list\x12$\n\x0c\x63lients_list\x12\x07.Client\x1a\x07.Client\"\x00\x30\x01\x32@\n\x0f\x43lient_messages\x12-\n\x0e\x63lient_message\x12\x07.Client\x1a\x0e.Message_reply\"\x00\x30\x01\x62\x06proto3')
)




_MESSAGE_REQUEST = _descriptor.Descriptor(
  name='Message_request',
  full_name='Message_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Message_request.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='Message_request.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='Message_request.time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_dest', full_name='Message_request.id_dest', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=17,
  serialized_end=90,
)


_MESSAGE_REPLY = _descriptor.Descriptor(
  name='Message_reply',
  full_name='Message_reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Message_reply.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='Message_reply.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='Message_reply.time', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=92,
  serialized_end=146,
)


_CLIENT = _descriptor.Descriptor(
  name='Client',
  full_name='Client',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Client.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=148,
  serialized_end=168,
)


_NULL = _descriptor.Descriptor(
  name='Null',
  full_name='Null',
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
  serialized_start=170,
  serialized_end=176,
)

DESCRIPTOR.message_types_by_name['Message_request'] = _MESSAGE_REQUEST
DESCRIPTOR.message_types_by_name['Message_reply'] = _MESSAGE_REPLY
DESCRIPTOR.message_types_by_name['Client'] = _CLIENT
DESCRIPTOR.message_types_by_name['Null'] = _NULL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message_request = _reflection.GeneratedProtocolMessageType('Message_request', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE_REQUEST,
  '__module__' : 'mensaje_pb2'
  # @@protoc_insertion_point(class_scope:Message_request)
  })
_sym_db.RegisterMessage(Message_request)

Message_reply = _reflection.GeneratedProtocolMessageType('Message_reply', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE_REPLY,
  '__module__' : 'mensaje_pb2'
  # @@protoc_insertion_point(class_scope:Message_reply)
  })
_sym_db.RegisterMessage(Message_reply)

Client = _reflection.GeneratedProtocolMessageType('Client', (_message.Message,), {
  'DESCRIPTOR' : _CLIENT,
  '__module__' : 'mensaje_pb2'
  # @@protoc_insertion_point(class_scope:Client)
  })
_sym_db.RegisterMessage(Client)

Null = _reflection.GeneratedProtocolMessageType('Null', (_message.Message,), {
  'DESCRIPTOR' : _NULL,
  '__module__' : 'mensaje_pb2'
  # @@protoc_insertion_point(class_scope:Null)
  })
_sym_db.RegisterMessage(Null)



_SENDER = _descriptor.ServiceDescriptor(
  name='Sender',
  full_name='Sender',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=178,
  serialized_end=292,
  methods=[
  _descriptor.MethodDescriptor(
    name='send_message',
    full_name='Sender.send_message',
    index=0,
    containing_service=None,
    input_type=_MESSAGE_REQUEST,
    output_type=_MESSAGE_REPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='recept_message',
    full_name='Sender.recept_message',
    index=1,
    containing_service=None,
    input_type=_MESSAGE_REQUEST,
    output_type=_MESSAGE_REPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SENDER)

DESCRIPTOR.services_by_name['Sender'] = _SENDER


_CLIENTS_LIST = _descriptor.ServiceDescriptor(
  name='Clients_list',
  full_name='Clients_list',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=294,
  serialized_end=346,
  methods=[
  _descriptor.MethodDescriptor(
    name='clients_list',
    full_name='Clients_list.clients_list',
    index=0,
    containing_service=None,
    input_type=_CLIENT,
    output_type=_CLIENT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLIENTS_LIST)

DESCRIPTOR.services_by_name['Clients_list'] = _CLIENTS_LIST


_CLIENT_MESSAGES = _descriptor.ServiceDescriptor(
  name='Client_messages',
  full_name='Client_messages',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=348,
  serialized_end=412,
  methods=[
  _descriptor.MethodDescriptor(
    name='client_message',
    full_name='Client_messages.client_message',
    index=0,
    containing_service=None,
    input_type=_CLIENT,
    output_type=_MESSAGE_REPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLIENT_MESSAGES)

DESCRIPTOR.services_by_name['Client_messages'] = _CLIENT_MESSAGES

# @@protoc_insertion_point(module_scope)