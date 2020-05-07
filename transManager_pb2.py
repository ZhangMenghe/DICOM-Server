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
  serialized_pb=_b('\n\x12transManager.proto\x12\x08helmsley\"x\n\x0e\x63onfigResponse\x12\x34\n\x07\x63onfigs\x18\x01 \x03(\x0b\x32#.helmsley.configResponse.configInfo\x1a\x30\n\nconfigInfo\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"\xbf\x01\n\x0f\x64\x61tasetResponse\x12\x37\n\x08\x64\x61tasets\x18\x01 \x03(\x0b\x32%.helmsley.datasetResponse.datasetInfo\x1as\n\x0b\x64\x61tasetInfo\x12\x13\n\x0b\x66older_name\x18\x01 \x01(\t\x12\x14\n\x0cpatient_name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\x15\n\rphysican_name\x18\x04 \x01(\t\x12\x14\n\x0cmask_folders\x18\x05 \x03(\t\"\xea\x01\n\x0evolumeResponse\x12\x34\n\x07volumes\x18\x01 \x03(\x0b\x32#.helmsley.volumeResponse.volumeInfo\x1a\xa1\x01\n\nvolumeInfo\x12\x13\n\x0b\x66older_name\x18\x01 \x01(\t\x12\x11\n\tfile_nums\x18\x02 \x01(\x05\x12\x11\n\timg_width\x18\x03 \x01(\x05\x12\x12\n\nimg_height\x18\x04 \x01(\x05\x12\x15\n\rvol_thickness\x18\x05 \x01(\x02\x12\x16\n\x0emask_available\x18\x06 \x01(\x08\x12\x15\n\rquality_score\x18\x07 \x01(\x02\"#\n\x13volumeWholeResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"9\n\x08\x64\x63mImage\x12\r\n\x05\x64\x63mID\x18\x01 \x01(\x05\x12\x10\n\x08position\x18\x02 \x01(\x02\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"-\n\x07Request\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12\x0f\n\x07req_msg\x18\x02 \x01(\t\"K\n\x12RequestWholeVolume\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12\x0f\n\x07req_msg\x18\x02 \x01(\t\x12\x11\n\tunit_size\x18\x03 \x01(\x05\",\n\x08Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07res_msg\x18\x02 \x01(\t2\xa0\x04\n\x0c\x64\x61taTransfer\x12\x42\n\x13getAvailableConfigs\x12\x11.helmsley.Request\x1a\x18.helmsley.configResponse\x12\x36\n\rexportConfigs\x12\x11.helmsley.Request\x1a\x12.helmsley.Response\x12\x44\n\x14getAvailableDatasets\x12\x11.helmsley.Request\x1a\x19.helmsley.datasetResponse\x12\x43\n\x14getVolumeFromDataset\x12\x11.helmsley.Request\x1a\x18.helmsley.volumeResponse\x12\x33\n\x08\x44ownload\x12\x11.helmsley.Request\x1a\x12.helmsley.dcmImage0\x01\x12O\n\x0e\x44ownloadVolume\x12\x1c.helmsley.RequestWholeVolume\x1a\x1d.helmsley.volumeWholeResponse0\x01\x12\x38\n\rDownloadMasks\x12\x11.helmsley.Request\x1a\x12.helmsley.dcmImage0\x01\x12I\n\x13\x44ownloadMasksVolume\x12\x11.helmsley.Request\x1a\x1d.helmsley.volumeWholeResponse0\x01\x62\x06proto3')
)




_CONFIGRESPONSE_CONFIGINFO = _descriptor.Descriptor(
  name='configInfo',
  full_name='helmsley.configResponse.configInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_name', full_name='helmsley.configResponse.configInfo.file_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='helmsley.configResponse.configInfo.content', index=1,
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
  serialized_start=104,
  serialized_end=152,
)

_CONFIGRESPONSE = _descriptor.Descriptor(
  name='configResponse',
  full_name='helmsley.configResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='configs', full_name='helmsley.configResponse.configs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONFIGRESPONSE_CONFIGINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=152,
)


_DATASETRESPONSE_DATASETINFO = _descriptor.Descriptor(
  name='datasetInfo',
  full_name='helmsley.datasetResponse.datasetInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_name', full_name='helmsley.datasetResponse.datasetInfo.folder_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patient_name', full_name='helmsley.datasetResponse.datasetInfo.patient_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='helmsley.datasetResponse.datasetInfo.date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='physican_name', full_name='helmsley.datasetResponse.datasetInfo.physican_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mask_folders', full_name='helmsley.datasetResponse.datasetInfo.mask_folders', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=231,
  serialized_end=346,
)

_DATASETRESPONSE = _descriptor.Descriptor(
  name='datasetResponse',
  full_name='helmsley.datasetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datasets', full_name='helmsley.datasetResponse.datasets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DATASETRESPONSE_DATASETINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=346,
)


_VOLUMERESPONSE_VOLUMEINFO = _descriptor.Descriptor(
  name='volumeInfo',
  full_name='helmsley.volumeResponse.volumeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_name', full_name='helmsley.volumeResponse.volumeInfo.folder_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_nums', full_name='helmsley.volumeResponse.volumeInfo.file_nums', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_width', full_name='helmsley.volumeResponse.volumeInfo.img_width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_height', full_name='helmsley.volumeResponse.volumeInfo.img_height', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vol_thickness', full_name='helmsley.volumeResponse.volumeInfo.vol_thickness', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mask_available', full_name='helmsley.volumeResponse.volumeInfo.mask_available', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quality_score', full_name='helmsley.volumeResponse.volumeInfo.quality_score', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=422,
  serialized_end=583,
)

_VOLUMERESPONSE = _descriptor.Descriptor(
  name='volumeResponse',
  full_name='helmsley.volumeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='volumes', full_name='helmsley.volumeResponse.volumes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VOLUMERESPONSE_VOLUMEINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=583,
)


_VOLUMEWHOLERESPONSE = _descriptor.Descriptor(
  name='volumeWholeResponse',
  full_name='helmsley.volumeWholeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='helmsley.volumeWholeResponse.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  serialized_start=585,
  serialized_end=620,
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
  serialized_start=622,
  serialized_end=679,
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
  serialized_start=681,
  serialized_end=726,
)


_REQUESTWHOLEVOLUME = _descriptor.Descriptor(
  name='RequestWholeVolume',
  full_name='helmsley.RequestWholeVolume',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='helmsley.RequestWholeVolume.client_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='req_msg', full_name='helmsley.RequestWholeVolume.req_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit_size', full_name='helmsley.RequestWholeVolume.unit_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=728,
  serialized_end=803,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='helmsley.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='helmsley.Response.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=805,
  serialized_end=849,
)

_CONFIGRESPONSE_CONFIGINFO.containing_type = _CONFIGRESPONSE
_CONFIGRESPONSE.fields_by_name['configs'].message_type = _CONFIGRESPONSE_CONFIGINFO
_DATASETRESPONSE_DATASETINFO.containing_type = _DATASETRESPONSE
_DATASETRESPONSE.fields_by_name['datasets'].message_type = _DATASETRESPONSE_DATASETINFO
_VOLUMERESPONSE_VOLUMEINFO.containing_type = _VOLUMERESPONSE
_VOLUMERESPONSE.fields_by_name['volumes'].message_type = _VOLUMERESPONSE_VOLUMEINFO
DESCRIPTOR.message_types_by_name['configResponse'] = _CONFIGRESPONSE
DESCRIPTOR.message_types_by_name['datasetResponse'] = _DATASETRESPONSE
DESCRIPTOR.message_types_by_name['volumeResponse'] = _VOLUMERESPONSE
DESCRIPTOR.message_types_by_name['volumeWholeResponse'] = _VOLUMEWHOLERESPONSE
DESCRIPTOR.message_types_by_name['dcmImage'] = _DCMIMAGE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['RequestWholeVolume'] = _REQUESTWHOLEVOLUME
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

configResponse = _reflection.GeneratedProtocolMessageType('configResponse', (_message.Message,), dict(

  configInfo = _reflection.GeneratedProtocolMessageType('configInfo', (_message.Message,), dict(
    DESCRIPTOR = _CONFIGRESPONSE_CONFIGINFO,
    __module__ = 'transManager_pb2'
    # @@protoc_insertion_point(class_scope:helmsley.configResponse.configInfo)
    ))
  ,
  DESCRIPTOR = _CONFIGRESPONSE,
  __module__ = 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.configResponse)
  ))
_sym_db.RegisterMessage(configResponse)
_sym_db.RegisterMessage(configResponse.configInfo)

datasetResponse = _reflection.GeneratedProtocolMessageType('datasetResponse', (_message.Message,), dict(

  datasetInfo = _reflection.GeneratedProtocolMessageType('datasetInfo', (_message.Message,), dict(
    DESCRIPTOR = _DATASETRESPONSE_DATASETINFO,
    __module__ = 'transManager_pb2'
    # @@protoc_insertion_point(class_scope:helmsley.datasetResponse.datasetInfo)
    ))
  ,
  DESCRIPTOR = _DATASETRESPONSE,
  __module__ = 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.datasetResponse)
  ))
_sym_db.RegisterMessage(datasetResponse)
_sym_db.RegisterMessage(datasetResponse.datasetInfo)

volumeResponse = _reflection.GeneratedProtocolMessageType('volumeResponse', (_message.Message,), dict(

  volumeInfo = _reflection.GeneratedProtocolMessageType('volumeInfo', (_message.Message,), dict(
    DESCRIPTOR = _VOLUMERESPONSE_VOLUMEINFO,
    __module__ = 'transManager_pb2'
    # @@protoc_insertion_point(class_scope:helmsley.volumeResponse.volumeInfo)
    ))
  ,
  DESCRIPTOR = _VOLUMERESPONSE,
  __module__ = 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.volumeResponse)
  ))
_sym_db.RegisterMessage(volumeResponse)
_sym_db.RegisterMessage(volumeResponse.volumeInfo)

volumeWholeResponse = _reflection.GeneratedProtocolMessageType('volumeWholeResponse', (_message.Message,), dict(
  DESCRIPTOR = _VOLUMEWHOLERESPONSE,
  __module__ = 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.volumeWholeResponse)
  ))
_sym_db.RegisterMessage(volumeWholeResponse)

dcmImage = _reflection.GeneratedProtocolMessageType('dcmImage', (_message.Message,), dict(
  DESCRIPTOR = _DCMIMAGE,
  __module__ = 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.dcmImage)
  ))
_sym_db.RegisterMessage(dcmImage)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.Request)
  ))
_sym_db.RegisterMessage(Request)

RequestWholeVolume = _reflection.GeneratedProtocolMessageType('RequestWholeVolume', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTWHOLEVOLUME,
  __module__ = 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.RequestWholeVolume)
  ))
_sym_db.RegisterMessage(RequestWholeVolume)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.Response)
  ))
_sym_db.RegisterMessage(Response)



_DATATRANSFER = _descriptor.ServiceDescriptor(
  name='dataTransfer',
  full_name='helmsley.dataTransfer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=852,
  serialized_end=1396,
  methods=[
  _descriptor.MethodDescriptor(
    name='getAvailableConfigs',
    full_name='helmsley.dataTransfer.getAvailableConfigs',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_CONFIGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='exportConfigs',
    full_name='helmsley.dataTransfer.exportConfigs',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getAvailableDatasets',
    full_name='helmsley.dataTransfer.getAvailableDatasets',
    index=2,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_DATASETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getVolumeFromDataset',
    full_name='helmsley.dataTransfer.getVolumeFromDataset',
    index=3,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_VOLUMERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Download',
    full_name='helmsley.dataTransfer.Download',
    index=4,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_DCMIMAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DownloadVolume',
    full_name='helmsley.dataTransfer.DownloadVolume',
    index=5,
    containing_service=None,
    input_type=_REQUESTWHOLEVOLUME,
    output_type=_VOLUMEWHOLERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DownloadMasks',
    full_name='helmsley.dataTransfer.DownloadMasks',
    index=6,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_DCMIMAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DownloadMasksVolume',
    full_name='helmsley.dataTransfer.DownloadMasksVolume',
    index=7,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_VOLUMEWHOLERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATATRANSFER)

DESCRIPTOR.services_by_name['dataTransfer'] = _DATATRANSFER

# @@protoc_insertion_point(module_scope)
