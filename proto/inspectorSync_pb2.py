# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inspectorSync.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='inspectorSync.proto',
  package='helmsley',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13inspectorSync.proto\x12\x08helmsley\x1a\x0c\x63ommon.proto\"\xa8\x01\n\x05VPMsg\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12#\n\x08req_type\x18\x02 \x01(\x0e\x32\x11.helmsley.ReqType\x12\x30\n\x10volume_pose_type\x18\x03 \x01(\x0e\x32\x16.helmsley.VPMsg.VPType\x12\x0e\n\x06values\x18\x04 \x03(\x02\"%\n\x06VPType\x12\x07\n\x03POS\x10\x00\x12\t\n\x05SCALE\x10\x01\x12\x07\n\x03ROT\x10\x02\"\xa4\x01\n\tGestureOp\x12\x0b\n\x03gid\x18\x01 \x01(\x03\x12(\n\x04type\x18\x02 \x01(\x0e\x32\x1a.helmsley.GestureOp.OPType\x12\t\n\x01x\x18\x03 \x01(\x02\x12\t\n\x01y\x18\x04 \x01(\x02\"J\n\x06OPType\x12\x0e\n\nTOUCH_DOWN\x10\x00\x12\x0c\n\x08TOUCH_UP\x10\x01\x12\x0e\n\nTOUCH_MOVE\x10\x02\x12\t\n\x05SCALE\x10\x03\x12\x07\n\x03PAN\x10\x04\"F\n\x0eOperationBatch\x12\x0b\n\x03\x62id\x18\x01 \x01(\x02\x12\'\n\ngesture_op\x18\x02 \x03(\x0b\x32\x13.helmsley.GestureOp\"^\n\x08ResetMsg\x12\x12\n\ncheck_keys\x18\x01 \x03(\t\x12\x14\n\x0c\x63heck_values\x18\x02 \x03(\x08\x12\x13\n\x0bvolume_pose\x18\x03 \x03(\x02\x12\x13\n\x0b\x63\x61mera_pose\x18\x04 \x03(\x02\"\x8c\x02\n\x07TuneMsg\x12(\n\x04type\x18\x01 \x01(\x0e\x32\x1a.helmsley.TuneMsg.TuneType\x12\x0e\n\x06target\x18\x02 \x01(\x05\x12\x12\n\nsub_target\x18\x03 \x01(\x05\x12\r\n\x05value\x18\x04 \x01(\x02\x12\x0e\n\x06values\x18\x05 \x03(\x02\"\x93\x01\n\x08TuneType\x12\x0b\n\x07\x41\x44\x44_ONE\x10\x00\x12\x0e\n\nREMOVE_ONE\x10\x01\x12\x0e\n\nREMOTE_ALL\x10\x02\x12\x0b\n\x07SET_ONE\x10\x03\x12\x0b\n\x07SET_ALL\x10\x04\x12\x0f\n\x0bSET_VISIBLE\x10\x05\x12\x0e\n\nSET_TARGET\x10\x06\x12\r\n\tCUT_PLANE\x10\x07\x12\x10\n\x0c\x43OLOR_SCHEME\x10\x08\"&\n\x08\x43heckMsg\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08\"%\n\x07MaskMsg\x12\x0b\n\x03num\x18\x01 \x01(\x05\x12\r\n\x05mbits\x18\x02 \x01(\x05\"P\n\rvolumeConcise\x12\x10\n\x08vol_path\x18\x01 \x01(\t\x12\x0c\n\x04\x64ims\x18\x02 \x03(\x05\x12\x0c\n\x04size\x18\x03 \x03(\x02\x12\x11\n\twith_mask\x18\x04 \x01(\x08\"\xf7\x02\n\x0e\x46rameUpdateMsg\x12/\n\x05types\x18\x01 \x03(\x0e\x32 .helmsley.FrameUpdateMsg.MsgType\x12%\n\x08gestures\x18\x02 \x03(\x0b\x32\x13.helmsley.GestureOp\x12 \n\x05tunes\x18\x03 \x03(\x0b\x32\x11.helmsley.TuneMsg\x12\"\n\x06\x63hecks\x18\x04 \x03(\x0b\x32\x12.helmsley.CheckMsg\x12%\n\nmask_value\x18\x05 \x01(\x0b\x32\x11.helmsley.MaskMsg\x12\'\n\x0breset_value\x18\x06 \x01(\x0b\x32\x12.helmsley.ResetMsg\x12+\n\ndata_value\x18\x07 \x01(\x0b\x32\x17.helmsley.volumeConcise\"J\n\x07MsgType\x12\x0b\n\x07GESTURE\x10\x00\x12\x08\n\x04TUNE\x10\x01\x12\t\n\x05\x43HECK\x10\x02\x12\x08\n\x04MASK\x10\x03\x12\t\n\x05RESET\x10\x04\x12\x08\n\x04\x44\x41TA\x10\x05*\x1b\n\x07ReqType\x12\x07\n\x03SET\x10\x00\x12\x07\n\x03GET\x10\x01\x32\xd2\x04\n\rinspectorSync\x12+\n\x0estartBroadcast\x12\x08.Request\x1a\x0f.commonResponse\x12\x32\n\x15startReceiveBroadcast\x12\x08.Request\x1a\x0f.commonResponse\x12\x30\n\x0cgsVolumePose\x12\x0f.helmsley.VPMsg\x1a\x0f.commonResponse\x12\x33\n\rgetOperations\x12\x08.Request\x1a\x18.helmsley.OperationBatch\x12\x30\n\ngetUpdates\x12\x08.Request\x1a\x18.helmsley.FrameUpdateMsg\x12\x32\n\x0breqestReset\x12\x12.helmsley.ResetMsg\x1a\x0f.commonResponse\x12\x34\n\x0csetGestureOp\x12\x13.helmsley.GestureOp\x1a\x0f.commonResponse\x12\x33\n\rsetTuneParams\x12\x11.helmsley.TuneMsg\x1a\x0f.commonResponse\x12\x35\n\x0esetCheckParams\x12\x12.helmsley.CheckMsg\x1a\x0f.commonResponse\x12\x33\n\rsetMaskParams\x12\x11.helmsley.MaskMsg\x1a\x0f.commonResponse\x12<\n\x10setDisplayVolume\x12\x17.helmsley.volumeConcise\x1a\x0f.commonResponseb\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])

_REQTYPE = _descriptor.EnumDescriptor(
  name='ReqType',
  full_name='helmsley.ReqType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1363,
  serialized_end=1390,
)
_sym_db.RegisterEnumDescriptor(_REQTYPE)

ReqType = enum_type_wrapper.EnumTypeWrapper(_REQTYPE)
SET = 0
GET = 1


_VPMSG_VPTYPE = _descriptor.EnumDescriptor(
  name='VPType',
  full_name='helmsley.VPMsg.VPType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCALE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=179,
  serialized_end=216,
)
_sym_db.RegisterEnumDescriptor(_VPMSG_VPTYPE)

_GESTUREOP_OPTYPE = _descriptor.EnumDescriptor(
  name='OPType',
  full_name='helmsley.GestureOp.OPType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TOUCH_DOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOUCH_UP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOUCH_MOVE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCALE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAN', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=309,
  serialized_end=383,
)
_sym_db.RegisterEnumDescriptor(_GESTUREOP_OPTYPE)

_TUNEMSG_TUNETYPE = _descriptor.EnumDescriptor(
  name='TuneType',
  full_name='helmsley.TuneMsg.TuneType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADD_ONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_ONE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_ALL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_ONE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_ALL', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_VISIBLE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_TARGET', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUT_PLANE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR_SCHEME', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=675,
  serialized_end=822,
)
_sym_db.RegisterEnumDescriptor(_TUNEMSG_TUNETYPE)

_FRAMEUPDATEMSG_MSGTYPE = _descriptor.EnumDescriptor(
  name='MsgType',
  full_name='helmsley.FrameUpdateMsg.MsgType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GESTURE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TUNE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MASK', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESET', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1287,
  serialized_end=1361,
)
_sym_db.RegisterEnumDescriptor(_FRAMEUPDATEMSG_MSGTYPE)


_VPMSG = _descriptor.Descriptor(
  name='VPMsg',
  full_name='helmsley.VPMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='helmsley.VPMsg.client_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='req_type', full_name='helmsley.VPMsg.req_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume_pose_type', full_name='helmsley.VPMsg.volume_pose_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='helmsley.VPMsg.values', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VPMSG_VPTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=216,
)


_GESTUREOP = _descriptor.Descriptor(
  name='GestureOp',
  full_name='helmsley.GestureOp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gid', full_name='helmsley.GestureOp.gid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='helmsley.GestureOp.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='helmsley.GestureOp.x', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='helmsley.GestureOp.y', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GESTUREOP_OPTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=383,
)


_OPERATIONBATCH = _descriptor.Descriptor(
  name='OperationBatch',
  full_name='helmsley.OperationBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bid', full_name='helmsley.OperationBatch.bid', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gesture_op', full_name='helmsley.OperationBatch.gesture_op', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=385,
  serialized_end=455,
)


_RESETMSG = _descriptor.Descriptor(
  name='ResetMsg',
  full_name='helmsley.ResetMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='check_keys', full_name='helmsley.ResetMsg.check_keys', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='check_values', full_name='helmsley.ResetMsg.check_values', index=1,
      number=2, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume_pose', full_name='helmsley.ResetMsg.volume_pose', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='camera_pose', full_name='helmsley.ResetMsg.camera_pose', index=3,
      number=4, type=2, cpp_type=6, label=3,
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
  serialized_start=457,
  serialized_end=551,
)


_TUNEMSG = _descriptor.Descriptor(
  name='TuneMsg',
  full_name='helmsley.TuneMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='helmsley.TuneMsg.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='helmsley.TuneMsg.target', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sub_target', full_name='helmsley.TuneMsg.sub_target', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='helmsley.TuneMsg.value', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='helmsley.TuneMsg.values', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TUNEMSG_TUNETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=554,
  serialized_end=822,
)


_CHECKMSG = _descriptor.Descriptor(
  name='CheckMsg',
  full_name='helmsley.CheckMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='helmsley.CheckMsg.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='helmsley.CheckMsg.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=824,
  serialized_end=862,
)


_MASKMSG = _descriptor.Descriptor(
  name='MaskMsg',
  full_name='helmsley.MaskMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='helmsley.MaskMsg.num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mbits', full_name='helmsley.MaskMsg.mbits', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=864,
  serialized_end=901,
)


_VOLUMECONCISE = _descriptor.Descriptor(
  name='volumeConcise',
  full_name='helmsley.volumeConcise',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vol_path', full_name='helmsley.volumeConcise.vol_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dims', full_name='helmsley.volumeConcise.dims', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='helmsley.volumeConcise.size', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_mask', full_name='helmsley.volumeConcise.with_mask', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=903,
  serialized_end=983,
)


_FRAMEUPDATEMSG = _descriptor.Descriptor(
  name='FrameUpdateMsg',
  full_name='helmsley.FrameUpdateMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='types', full_name='helmsley.FrameUpdateMsg.types', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gestures', full_name='helmsley.FrameUpdateMsg.gestures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tunes', full_name='helmsley.FrameUpdateMsg.tunes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checks', full_name='helmsley.FrameUpdateMsg.checks', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mask_value', full_name='helmsley.FrameUpdateMsg.mask_value', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reset_value', full_name='helmsley.FrameUpdateMsg.reset_value', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_value', full_name='helmsley.FrameUpdateMsg.data_value', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FRAMEUPDATEMSG_MSGTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=986,
  serialized_end=1361,
)

_VPMSG.fields_by_name['req_type'].enum_type = _REQTYPE
_VPMSG.fields_by_name['volume_pose_type'].enum_type = _VPMSG_VPTYPE
_VPMSG_VPTYPE.containing_type = _VPMSG
_GESTUREOP.fields_by_name['type'].enum_type = _GESTUREOP_OPTYPE
_GESTUREOP_OPTYPE.containing_type = _GESTUREOP
_OPERATIONBATCH.fields_by_name['gesture_op'].message_type = _GESTUREOP
_TUNEMSG.fields_by_name['type'].enum_type = _TUNEMSG_TUNETYPE
_TUNEMSG_TUNETYPE.containing_type = _TUNEMSG
_FRAMEUPDATEMSG.fields_by_name['types'].enum_type = _FRAMEUPDATEMSG_MSGTYPE
_FRAMEUPDATEMSG.fields_by_name['gestures'].message_type = _GESTUREOP
_FRAMEUPDATEMSG.fields_by_name['tunes'].message_type = _TUNEMSG
_FRAMEUPDATEMSG.fields_by_name['checks'].message_type = _CHECKMSG
_FRAMEUPDATEMSG.fields_by_name['mask_value'].message_type = _MASKMSG
_FRAMEUPDATEMSG.fields_by_name['reset_value'].message_type = _RESETMSG
_FRAMEUPDATEMSG.fields_by_name['data_value'].message_type = _VOLUMECONCISE
_FRAMEUPDATEMSG_MSGTYPE.containing_type = _FRAMEUPDATEMSG
DESCRIPTOR.message_types_by_name['VPMsg'] = _VPMSG
DESCRIPTOR.message_types_by_name['GestureOp'] = _GESTUREOP
DESCRIPTOR.message_types_by_name['OperationBatch'] = _OPERATIONBATCH
DESCRIPTOR.message_types_by_name['ResetMsg'] = _RESETMSG
DESCRIPTOR.message_types_by_name['TuneMsg'] = _TUNEMSG
DESCRIPTOR.message_types_by_name['CheckMsg'] = _CHECKMSG
DESCRIPTOR.message_types_by_name['MaskMsg'] = _MASKMSG
DESCRIPTOR.message_types_by_name['volumeConcise'] = _VOLUMECONCISE
DESCRIPTOR.message_types_by_name['FrameUpdateMsg'] = _FRAMEUPDATEMSG
DESCRIPTOR.enum_types_by_name['ReqType'] = _REQTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VPMsg = _reflection.GeneratedProtocolMessageType('VPMsg', (_message.Message,), dict(
  DESCRIPTOR = _VPMSG,
  __module__ = 'inspectorSync_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.VPMsg)
  ))
_sym_db.RegisterMessage(VPMsg)

GestureOp = _reflection.GeneratedProtocolMessageType('GestureOp', (_message.Message,), dict(
  DESCRIPTOR = _GESTUREOP,
  __module__ = 'inspectorSync_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.GestureOp)
  ))
_sym_db.RegisterMessage(GestureOp)

OperationBatch = _reflection.GeneratedProtocolMessageType('OperationBatch', (_message.Message,), dict(
  DESCRIPTOR = _OPERATIONBATCH,
  __module__ = 'inspectorSync_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.OperationBatch)
  ))
_sym_db.RegisterMessage(OperationBatch)

ResetMsg = _reflection.GeneratedProtocolMessageType('ResetMsg', (_message.Message,), dict(
  DESCRIPTOR = _RESETMSG,
  __module__ = 'inspectorSync_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.ResetMsg)
  ))
_sym_db.RegisterMessage(ResetMsg)

TuneMsg = _reflection.GeneratedProtocolMessageType('TuneMsg', (_message.Message,), dict(
  DESCRIPTOR = _TUNEMSG,
  __module__ = 'inspectorSync_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.TuneMsg)
  ))
_sym_db.RegisterMessage(TuneMsg)

CheckMsg = _reflection.GeneratedProtocolMessageType('CheckMsg', (_message.Message,), dict(
  DESCRIPTOR = _CHECKMSG,
  __module__ = 'inspectorSync_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.CheckMsg)
  ))
_sym_db.RegisterMessage(CheckMsg)

MaskMsg = _reflection.GeneratedProtocolMessageType('MaskMsg', (_message.Message,), dict(
  DESCRIPTOR = _MASKMSG,
  __module__ = 'inspectorSync_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.MaskMsg)
  ))
_sym_db.RegisterMessage(MaskMsg)

volumeConcise = _reflection.GeneratedProtocolMessageType('volumeConcise', (_message.Message,), dict(
  DESCRIPTOR = _VOLUMECONCISE,
  __module__ = 'inspectorSync_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.volumeConcise)
  ))
_sym_db.RegisterMessage(volumeConcise)

FrameUpdateMsg = _reflection.GeneratedProtocolMessageType('FrameUpdateMsg', (_message.Message,), dict(
  DESCRIPTOR = _FRAMEUPDATEMSG,
  __module__ = 'inspectorSync_pb2'
  # @@protoc_insertion_point(class_scope:helmsley.FrameUpdateMsg)
  ))
_sym_db.RegisterMessage(FrameUpdateMsg)



_INSPECTORSYNC = _descriptor.ServiceDescriptor(
  name='inspectorSync',
  full_name='helmsley.inspectorSync',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1393,
  serialized_end=1987,
  methods=[
  _descriptor.MethodDescriptor(
    name='startBroadcast',
    full_name='helmsley.inspectorSync.startBroadcast',
    index=0,
    containing_service=None,
    input_type=common__pb2._REQUEST,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='startReceiveBroadcast',
    full_name='helmsley.inspectorSync.startReceiveBroadcast',
    index=1,
    containing_service=None,
    input_type=common__pb2._REQUEST,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='gsVolumePose',
    full_name='helmsley.inspectorSync.gsVolumePose',
    index=2,
    containing_service=None,
    input_type=_VPMSG,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getOperations',
    full_name='helmsley.inspectorSync.getOperations',
    index=3,
    containing_service=None,
    input_type=common__pb2._REQUEST,
    output_type=_OPERATIONBATCH,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getUpdates',
    full_name='helmsley.inspectorSync.getUpdates',
    index=4,
    containing_service=None,
    input_type=common__pb2._REQUEST,
    output_type=_FRAMEUPDATEMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='reqestReset',
    full_name='helmsley.inspectorSync.reqestReset',
    index=5,
    containing_service=None,
    input_type=_RESETMSG,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='setGestureOp',
    full_name='helmsley.inspectorSync.setGestureOp',
    index=6,
    containing_service=None,
    input_type=_GESTUREOP,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='setTuneParams',
    full_name='helmsley.inspectorSync.setTuneParams',
    index=7,
    containing_service=None,
    input_type=_TUNEMSG,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='setCheckParams',
    full_name='helmsley.inspectorSync.setCheckParams',
    index=8,
    containing_service=None,
    input_type=_CHECKMSG,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='setMaskParams',
    full_name='helmsley.inspectorSync.setMaskParams',
    index=9,
    containing_service=None,
    input_type=_MASKMSG,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='setDisplayVolume',
    full_name='helmsley.inspectorSync.setDisplayVolume',
    index=10,
    containing_service=None,
    input_type=_VOLUMECONCISE,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_INSPECTORSYNC)

DESCRIPTOR.services_by_name['inspectorSync'] = _INSPECTORSYNC

# @@protoc_insertion_point(module_scope)
