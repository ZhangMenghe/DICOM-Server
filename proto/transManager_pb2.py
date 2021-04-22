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


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='transManager.proto',
  package='helmsley',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12transManager.proto\x12\x08helmsley\x1a\x0c\x63ommon.proto\"x\n\x0e\x63onfigResponse\x12\x34\n\x07\x63onfigs\x18\x01 \x03(\x0b\x32#.helmsley.configResponse.configInfo\x1a\x30\n\nconfigInfo\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"\xbf\x01\n\x0f\x64\x61tasetResponse\x12\x37\n\x08\x64\x61tasets\x18\x01 \x03(\x0b\x32%.helmsley.datasetResponse.datasetInfo\x1as\n\x0b\x64\x61tasetInfo\x12\x13\n\x0b\x66older_name\x18\x01 \x01(\t\x12\x14\n\x0cpatient_name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\x15\n\rphysican_name\x18\x04 \x01(\t\x12\x14\n\x0cmask_folders\x18\x05 \x03(\t\"7\n\x0evolumeResponse\x12%\n\x07volumes\x18\x01 \x03(\x0b\x32\x14.helmsley.volumeInfo\"#\n\x13volumeWholeResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x1e\n\x0e\x63\x65nterlineData\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x02\"9\n\x08\x64\x63mImage\x12\r\n\x05\x64\x63mID\x18\x01 \x01(\x05\x12\x10\n\x08position\x18\x02 \x01(\x02\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"K\n\x12RequestWholeVolume\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12\x0f\n\x07req_msg\x18\x02 \x01(\t\x12\x11\n\tunit_size\x18\x03 \x01(\x05\x32\xf1\x04\n\x0c\x64\x61taTransfer\x12\x42\n\x13getAvailableConfigs\x12\x11.helmsley.Request\x1a\x18.helmsley.configResponse\x12<\n\rexportConfigs\x12\x11.helmsley.Request\x1a\x18.helmsley.commonResponse\x12\x44\n\x14getAvailableDatasets\x12\x11.helmsley.Request\x1a\x19.helmsley.datasetResponse\x12\x45\n\x14getVolumeFromDataset\x12\x11.helmsley.Request\x1a\x18.helmsley.volumeResponse0\x01\x12\x33\n\x08\x44ownload\x12\x11.helmsley.Request\x1a\x12.helmsley.dcmImage0\x01\x12O\n\x0e\x44ownloadVolume\x12\x1c.helmsley.RequestWholeVolume\x1a\x1d.helmsley.volumeWholeResponse0\x01\x12\x38\n\rDownloadMasks\x12\x11.helmsley.Request\x1a\x12.helmsley.dcmImage0\x01\x12I\n\x13\x44ownloadMasksVolume\x12\x11.helmsley.Request\x1a\x1d.helmsley.volumeWholeResponse0\x01\x12G\n\x16\x44ownloadCenterLineData\x12\x11.helmsley.Request\x1a\x18.helmsley.centerlineData0\x01\x62\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




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
  serialized_start=118,
  serialized_end=166,
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
  serialized_start=46,
  serialized_end=166,
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
  serialized_start=245,
  serialized_end=360,
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
  serialized_start=169,
  serialized_end=360,
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
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=362,
  serialized_end=417,
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
  serialized_start=419,
  serialized_end=454,
)


_CENTERLINEDATA = _descriptor.Descriptor(
  name='centerlineData',
  full_name='helmsley.centerlineData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='helmsley.centerlineData.data', index=0,
      number=1, type=2, cpp_type=6, label=3,
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
  serialized_start=456,
  serialized_end=486,
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
  serialized_start=488,
  serialized_end=545,
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
  serialized_start=547,
  serialized_end=622,
)

_CONFIGRESPONSE_CONFIGINFO.containing_type = _CONFIGRESPONSE
_CONFIGRESPONSE.fields_by_name['configs'].message_type = _CONFIGRESPONSE_CONFIGINFO
_DATASETRESPONSE_DATASETINFO.containing_type = _DATASETRESPONSE
_DATASETRESPONSE.fields_by_name['datasets'].message_type = _DATASETRESPONSE_DATASETINFO
_VOLUMERESPONSE.fields_by_name['volumes'].message_type = common__pb2._VOLUMEINFO
DESCRIPTOR.message_types_by_name['configResponse'] = _CONFIGRESPONSE
DESCRIPTOR.message_types_by_name['datasetResponse'] = _DATASETRESPONSE
DESCRIPTOR.message_types_by_name['volumeResponse'] = _VOLUMERESPONSE
DESCRIPTOR.message_types_by_name['volumeWholeResponse'] = _VOLUMEWHOLERESPONSE
DESCRIPTOR.message_types_by_name['centerlineData'] = _CENTERLINEDATA
DESCRIPTOR.message_types_by_name['dcmImage'] = _DCMIMAGE
DESCRIPTOR.message_types_by_name['RequestWholeVolume'] = _REQUESTWHOLEVOLUME
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
  DESCRIPTOR = _VOLUMERESPONSE,
  __module__ = 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.volumeResponse)
  ))
_sym_db.RegisterMessage(volumeResponse)

volumeWholeResponse = _reflection.GeneratedProtocolMessageType('volumeWholeResponse', (_message.Message,), dict(
  DESCRIPTOR = _VOLUMEWHOLERESPONSE,
  __module__ = 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.volumeWholeResponse)
  ))
_sym_db.RegisterMessage(volumeWholeResponse)

centerlineData = _reflection.GeneratedProtocolMessageType('centerlineData', (_message.Message,), dict(
  DESCRIPTOR = _CENTERLINEDATA,
  __module__ = 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.centerlineData)
  ))
_sym_db.RegisterMessage(centerlineData)

dcmImage = _reflection.GeneratedProtocolMessageType('dcmImage', (_message.Message,), dict(
  DESCRIPTOR = _DCMIMAGE,
  __module__ = 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.dcmImage)
  ))
_sym_db.RegisterMessage(dcmImage)

RequestWholeVolume = _reflection.GeneratedProtocolMessageType('RequestWholeVolume', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTWHOLEVOLUME,
  __module__ = 'transManager_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.RequestWholeVolume)
  ))
_sym_db.RegisterMessage(RequestWholeVolume)



_DATATRANSFER = _descriptor.ServiceDescriptor(
  name='dataTransfer',
  full_name='helmsley.dataTransfer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=625,
  serialized_end=1250,
  methods=[
  _descriptor.MethodDescriptor(
    name='getAvailableConfigs',
    full_name='helmsley.dataTransfer.getAvailableConfigs',
    index=0,
    containing_service=None,
    input_type=common__pb2._REQUEST,
    output_type=_CONFIGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='exportConfigs',
    full_name='helmsley.dataTransfer.exportConfigs',
    index=1,
    containing_service=None,
    input_type=common__pb2._REQUEST,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getAvailableDatasets',
    full_name='helmsley.dataTransfer.getAvailableDatasets',
    index=2,
    containing_service=None,
    input_type=common__pb2._REQUEST,
    output_type=_DATASETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getVolumeFromDataset',
    full_name='helmsley.dataTransfer.getVolumeFromDataset',
    index=3,
    containing_service=None,
    input_type=common__pb2._REQUEST,
    output_type=_VOLUMERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Download',
    full_name='helmsley.dataTransfer.Download',
    index=4,
    containing_service=None,
    input_type=common__pb2._REQUEST,
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
    input_type=common__pb2._REQUEST,
    output_type=_DCMIMAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DownloadMasksVolume',
    full_name='helmsley.dataTransfer.DownloadMasksVolume',
    index=7,
    containing_service=None,
    input_type=common__pb2._REQUEST,
    output_type=_VOLUMEWHOLERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DownloadCenterLineData',
    full_name='helmsley.dataTransfer.DownloadCenterLineData',
    index=8,
    containing_service=None,
    input_type=common__pb2._REQUEST,
    output_type=_CENTERLINEDATA,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATATRANSFER)

DESCRIPTOR.services_by_name['dataTransfer'] = _DATATRANSFER

# @@protoc_insertion_point(module_scope)
