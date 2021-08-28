# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import common_pb2 as common__pb2
import inspectorSync_pb2 as inspectorSync__pb2


class inspectorSyncStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.startBroadcast = channel.unary_unary(
        '/helmsley.inspectorSync/startBroadcast',
        request_serializer=common__pb2.Request.SerializeToString,
        response_deserializer=common__pb2.commonResponse.FromString,
        )
    self.startReceiveBroadcast = channel.unary_unary(
        '/helmsley.inspectorSync/startReceiveBroadcast',
        request_serializer=common__pb2.Request.SerializeToString,
        response_deserializer=common__pb2.commonResponse.FromString,
        )
    self.reqestReset = channel.unary_unary(
        '/helmsley.inspectorSync/reqestReset',
        request_serializer=inspectorSync__pb2.ResetMsg.SerializeToString,
        response_deserializer=common__pb2.commonResponse.FromString,
        )
    self.getVolumePoses = channel.unary_unary(
        '/helmsley.inspectorSync/getVolumePoses',
        request_serializer=common__pb2.Request.SerializeToString,
        response_deserializer=inspectorSync__pb2.VolumePoseBatch.FromString,
        )
    self.getOperations = channel.unary_unary(
        '/helmsley.inspectorSync/getOperations',
        request_serializer=common__pb2.Request.SerializeToString,
        response_deserializer=inspectorSync__pb2.OperationBatch.FromString,
        )
    self.getUpdates = channel.unary_unary(
        '/helmsley.inspectorSync/getUpdates',
        request_serializer=common__pb2.Request.SerializeToString,
        response_deserializer=inspectorSync__pb2.FrameUpdateMsg.FromString,
        )
    self.setVolumePose = channel.unary_unary(
        '/helmsley.inspectorSync/setVolumePose',
        request_serializer=inspectorSync__pb2.VPMsg.SerializeToString,
        response_deserializer=common__pb2.commonResponse.FromString,
        )
    self.setGestureOp = channel.unary_unary(
        '/helmsley.inspectorSync/setGestureOp',
        request_serializer=inspectorSync__pb2.GestureOp.SerializeToString,
        response_deserializer=common__pb2.commonResponse.FromString,
        )
    self.setTuneParams = channel.unary_unary(
        '/helmsley.inspectorSync/setTuneParams',
        request_serializer=inspectorSync__pb2.TuneMsg.SerializeToString,
        response_deserializer=common__pb2.commonResponse.FromString,
        )
    self.setCheckParams = channel.unary_unary(
        '/helmsley.inspectorSync/setCheckParams',
        request_serializer=inspectorSync__pb2.CheckMsg.SerializeToString,
        response_deserializer=common__pb2.commonResponse.FromString,
        )
    self.setMaskParams = channel.unary_unary(
        '/helmsley.inspectorSync/setMaskParams',
        request_serializer=inspectorSync__pb2.MaskMsg.SerializeToString,
        response_deserializer=common__pb2.commonResponse.FromString,
        )
    self.setDisplayVolume = channel.unary_unary(
        '/helmsley.inspectorSync/setDisplayVolume',
        request_serializer=inspectorSync__pb2.DataMsg.SerializeToString,
        response_deserializer=common__pb2.commonResponse.FromString,
        )


class inspectorSyncServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def startBroadcast(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def startReceiveBroadcast(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def reqestReset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getVolumePoses(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getOperations(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getUpdates(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def setVolumePose(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def setGestureOp(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def setTuneParams(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def setCheckParams(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def setMaskParams(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def setDisplayVolume(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_inspectorSyncServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'startBroadcast': grpc.unary_unary_rpc_method_handler(
          servicer.startBroadcast,
          request_deserializer=common__pb2.Request.FromString,
          response_serializer=common__pb2.commonResponse.SerializeToString,
      ),
      'startReceiveBroadcast': grpc.unary_unary_rpc_method_handler(
          servicer.startReceiveBroadcast,
          request_deserializer=common__pb2.Request.FromString,
          response_serializer=common__pb2.commonResponse.SerializeToString,
      ),
      'reqestReset': grpc.unary_unary_rpc_method_handler(
          servicer.reqestReset,
          request_deserializer=inspectorSync__pb2.ResetMsg.FromString,
          response_serializer=common__pb2.commonResponse.SerializeToString,
      ),
      'getVolumePoses': grpc.unary_unary_rpc_method_handler(
          servicer.getVolumePoses,
          request_deserializer=common__pb2.Request.FromString,
          response_serializer=inspectorSync__pb2.VolumePoseBatch.SerializeToString,
      ),
      'getOperations': grpc.unary_unary_rpc_method_handler(
          servicer.getOperations,
          request_deserializer=common__pb2.Request.FromString,
          response_serializer=inspectorSync__pb2.OperationBatch.SerializeToString,
      ),
      'getUpdates': grpc.unary_unary_rpc_method_handler(
          servicer.getUpdates,
          request_deserializer=common__pb2.Request.FromString,
          response_serializer=inspectorSync__pb2.FrameUpdateMsg.SerializeToString,
      ),
      'setVolumePose': grpc.unary_unary_rpc_method_handler(
          servicer.setVolumePose,
          request_deserializer=inspectorSync__pb2.VPMsg.FromString,
          response_serializer=common__pb2.commonResponse.SerializeToString,
      ),
      'setGestureOp': grpc.unary_unary_rpc_method_handler(
          servicer.setGestureOp,
          request_deserializer=inspectorSync__pb2.GestureOp.FromString,
          response_serializer=common__pb2.commonResponse.SerializeToString,
      ),
      'setTuneParams': grpc.unary_unary_rpc_method_handler(
          servicer.setTuneParams,
          request_deserializer=inspectorSync__pb2.TuneMsg.FromString,
          response_serializer=common__pb2.commonResponse.SerializeToString,
      ),
      'setCheckParams': grpc.unary_unary_rpc_method_handler(
          servicer.setCheckParams,
          request_deserializer=inspectorSync__pb2.CheckMsg.FromString,
          response_serializer=common__pb2.commonResponse.SerializeToString,
      ),
      'setMaskParams': grpc.unary_unary_rpc_method_handler(
          servicer.setMaskParams,
          request_deserializer=inspectorSync__pb2.MaskMsg.FromString,
          response_serializer=common__pb2.commonResponse.SerializeToString,
      ),
      'setDisplayVolume': grpc.unary_unary_rpc_method_handler(
          servicer.setDisplayVolume,
          request_deserializer=inspectorSync__pb2.DataMsg.FromString,
          response_serializer=common__pb2.commonResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'helmsley.inspectorSync', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
