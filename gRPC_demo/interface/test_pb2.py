# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntest.proto\"\x19\n\tMyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x17\n\x07MyReply\x12\x0c\n\x04name\x18\x01 \x01(\t2\xc7\x01\n\x04Test\x12#\n\tUnaryRPCs\x12\n.MyRequest\x1a\x08.MyReply\"\x00\x12/\n\x13ServerStreamingRPCs\x12\n.MyRequest\x1a\x08.MyReply\"\x00\x30\x01\x12/\n\x13\x43lientStreamingRPCs\x12\n.MyRequest\x1a\x08.MyReply\"\x00(\x01\x12\x38\n\x1a\x42idirectionalStreamingRPCs\x12\n.MyRequest\x1a\x08.MyReply\"\x00(\x01\x30\x01\x62\x06proto3')
)




_MYREQUEST = _descriptor.Descriptor(
  name='MyRequest',
  full_name='MyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='MyRequest.name', index=0,
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
  serialized_start=14,
  serialized_end=39,
)


_MYREPLY = _descriptor.Descriptor(
  name='MyReply',
  full_name='MyReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='MyReply.name', index=0,
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
  serialized_start=41,
  serialized_end=64,
)

DESCRIPTOR.message_types_by_name['MyRequest'] = _MYREQUEST
DESCRIPTOR.message_types_by_name['MyReply'] = _MYREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MyRequest = _reflection.GeneratedProtocolMessageType('MyRequest', (_message.Message,), {
  'DESCRIPTOR' : _MYREQUEST,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:MyRequest)
  })
_sym_db.RegisterMessage(MyRequest)

MyReply = _reflection.GeneratedProtocolMessageType('MyReply', (_message.Message,), {
  'DESCRIPTOR' : _MYREPLY,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:MyReply)
  })
_sym_db.RegisterMessage(MyReply)



_TEST = _descriptor.ServiceDescriptor(
  name='Test',
  full_name='Test',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=67,
  serialized_end=266,
  methods=[
  _descriptor.MethodDescriptor(
    name='UnaryRPCs',
    full_name='Test.UnaryRPCs',
    index=0,
    containing_service=None,
    input_type=_MYREQUEST,
    output_type=_MYREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ServerStreamingRPCs',
    full_name='Test.ServerStreamingRPCs',
    index=1,
    containing_service=None,
    input_type=_MYREQUEST,
    output_type=_MYREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ClientStreamingRPCs',
    full_name='Test.ClientStreamingRPCs',
    index=2,
    containing_service=None,
    input_type=_MYREQUEST,
    output_type=_MYREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='BidirectionalStreamingRPCs',
    full_name='Test.BidirectionalStreamingRPCs',
    index=3,
    containing_service=None,
    input_type=_MYREQUEST,
    output_type=_MYREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEST)

DESCRIPTOR.services_by_name['Test'] = _TEST

# @@protoc_insertion_point(module_scope)
