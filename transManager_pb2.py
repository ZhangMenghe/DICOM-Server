# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transManager.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transManager.proto',
  package='helmsley',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12transManager.proto\x12\x08helmsley\"Y\n\x0b\x64\x61tasetInfo\x12\x13\n\x0b\x66older_name\x18\x01 \x01(\t\x12\x14\n\x0cpatient_name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\x11\n\tfile_nums\x18\x04 \x01(\x05\"9\n\x08\x64\x63mImage\x12\r\n\x05\x64\x63mID\x18\x01 \x01(\x05\x12\x10\n\x08position\x18\x02 \x01(\x02\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"t\n\x0c\x62undleConfig\x12\x13\n\x0b\x66older_name\x18\x01 \x01(\t\x12\x11\n\tfile_nums\x18\x02 \x01(\x05\x12\x11\n\timg_width\x18\x03 \x01(\x05\x12\x12\n\nimg_height\x18\x04 \x01(\x05\x12\x15\n\rorder_flipped\x18\x05 \x01(\x08\"-\n\x07Request\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12\x0f\n\x07req_msg\x18\x02 \x01(\t\".\n\x08Response\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12\x0f\n\x07res_msg\x18\x02 \x01(\t2\xc3\x01\n\x0c\x64\x61taTransfer\x12\x46\n\x18getAvailableDatasetInfos\x12\x11.helmsley.Request\x1a\x15.helmsley.datasetInfo0\x01\x12\x36\n\tgetConfig\x12\x11.helmsley.Request\x1a\x16.helmsley.bundleConfig\x12\x33\n\x08\x44ownload\x12\x11.helmsley.Request\x1a\x12.helmsley.dcmImage0\x01\x62\x06proto3')
)




_DATASETINFO = _descriptor.Descriptor(
  name='datasetInfo',
  full_name='helmsley.datasetInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_name', full_name='helmsley.datasetInfo.folder_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patient_name', full_name='helmsley.datasetInfo.patient_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='helmsley.datasetInfo.date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_nums', full_name='helmsley.datasetInfo.file_nums', index=3,
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
  serialized_start=32,
  serialized_end=121,
)


_DCMIMAGE = _descriptor.Descriptor(
  name='dcmImage',
  full_name='helmsley.dcmImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dcmID', full_name='helmsley.dcmImage.dcmID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='helmsley.dcmImage.position', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='helmsley.dcmImage.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=123,
  serialized_end=180,
)


_BUNDLECONFIG = _descriptor.Descriptor(
  name='bundleConfig',
  full_name='helmsley.bundleConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_name', full_name='helmsley.bundleConfig.folder_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_nums', full_name='helmsley.bundleConfig.file_nums', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_width', full_name='helmsley.bundleConfig.img_width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_height', full_name='helmsley.bundleConfig.img_height', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_flipped', full_name='helmsley.bundleConfig.order_flipped', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=182,
  serialized_end=298,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='helmsley.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='helmsley.Request.client_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='req_msg', full_name='helmsley.Request.req_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=300,
  serialized_end=345,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='helmsley.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='helmsley.Response.client_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='res_msg', full_name='helmsley.Response.res_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=347,
  serialized_end=393,
)

DESCRIPTOR.message_types_by_name['datasetInfo'] = _DATASETINFO
DESCRIPTOR.message_types_by_name['dcmImage'] = _DCMIMAGE
DESCRIPTOR.message_types_by_name['bundleConfig'] = _BUNDLECONFIG
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

datasetInfo = _reflection.GeneratedProtocolMessageType('datasetInfo', (_message.Message,), {
  'DESCRIPTOR' : _DATASETINFO,
  '__module__' : 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.datasetInfo)
  })
_sym_db.RegisterMessage(datasetInfo)

dcmImage = _reflection.GeneratedProtocolMessageType('dcmImage', (_message.Message,), {
  'DESCRIPTOR' : _DCMIMAGE,
  '__module__' : 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.dcmImage)
  })
_sym_db.RegisterMessage(dcmImage)

bundleConfig = _reflection.GeneratedProtocolMessageType('bundleConfig', (_message.Message,), {
  'DESCRIPTOR' : _BUNDLECONFIG,
  '__module__' : 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.bundleConfig)
  })
_sym_db.RegisterMessage(bundleConfig)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.Response)
  })
_sym_db.RegisterMessage(Response)



_DATATRANSFER = _descriptor.ServiceDescriptor(
  name='dataTransfer',
  full_name='helmsley.dataTransfer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=396,
  serialized_end=591,
  methods=[
  _descriptor.MethodDescriptor(
    name='getAvailableDatasetInfos',
    full_name='helmsley.dataTransfer.getAvailableDatasetInfos',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_DATASETINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getConfig',
    full_name='helmsley.dataTransfer.getConfig',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_BUNDLECONFIG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Download',
    full_name='helmsley.dataTransfer.Download',
    index=2,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_DCMIMAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATATRANSFER)

DESCRIPTOR.services_by_name['dataTransfer'] = _DATATRANSFER

# @@protoc_insertion_point(module_scope)
