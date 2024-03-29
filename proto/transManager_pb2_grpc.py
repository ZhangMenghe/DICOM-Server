# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import common_pb2 as common__pb2
import transManager_pb2 as transManager__pb2


class dataTransferStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getAvailableConfigs = channel.unary_unary(
        '/helmsley.dataTransfer/getAvailableConfigs',
        request_serializer=common__pb2.Request.SerializeToString,
        response_deserializer=transManager__pb2.configResponse.FromString,
        )
    self.exportConfigs = channel.unary_unary(
        '/helmsley.dataTransfer/exportConfigs',
        request_serializer=common__pb2.Request.SerializeToString,
        response_deserializer=common__pb2.commonResponse.FromString,
        )
    self.getAvailableDatasets = channel.unary_unary(
        '/helmsley.dataTransfer/getAvailableDatasets',
        request_serializer=common__pb2.Request.SerializeToString,
        response_deserializer=transManager__pb2.datasetResponse.FromString,
        )
    self.getVolumeFromDataset = channel.unary_stream(
        '/helmsley.dataTransfer/getVolumeFromDataset',
        request_serializer=common__pb2.Request.SerializeToString,
        response_deserializer=transManager__pb2.volumeResponse.FromString,
        )
    self.Download = channel.unary_stream(
        '/helmsley.dataTransfer/Download',
        request_serializer=common__pb2.Request.SerializeToString,
        response_deserializer=transManager__pb2.dcmImage.FromString,
        )
    self.DownloadVolume = channel.unary_stream(
        '/helmsley.dataTransfer/DownloadVolume',
        request_serializer=transManager__pb2.RequestWholeVolume.SerializeToString,
        response_deserializer=transManager__pb2.volumeWholeResponse.FromString,
        )
    self.DownloadVolumeProcessed = channel.unary_stream(
        '/helmsley.dataTransfer/DownloadVolumeProcessed',
        request_serializer=transManager__pb2.RequestWholeVolume.SerializeToString,
        response_deserializer=transManager__pb2.volumeWholeResponse.FromString,
        )
    self.DownloadMasks = channel.unary_stream(
        '/helmsley.dataTransfer/DownloadMasks',
        request_serializer=common__pb2.Request.SerializeToString,
        response_deserializer=transManager__pb2.dcmImage.FromString,
        )
    self.DownloadMasksVolume = channel.unary_stream(
        '/helmsley.dataTransfer/DownloadMasksVolume',
        request_serializer=common__pb2.Request.SerializeToString,
        response_deserializer=transManager__pb2.volumeWholeResponse.FromString,
        )
    self.DownloadCenterLineData = channel.unary_stream(
        '/helmsley.dataTransfer/DownloadCenterLineData',
        request_serializer=common__pb2.Request.SerializeToString,
        response_deserializer=transManager__pb2.centerlineData.FromString,
        )


class dataTransferServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def getAvailableConfigs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def exportConfigs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getAvailableDatasets(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getVolumeFromDataset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Download(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DownloadVolume(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DownloadVolumeProcessed(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DownloadMasks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DownloadMasksVolume(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DownloadCenterLineData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_dataTransferServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getAvailableConfigs': grpc.unary_unary_rpc_method_handler(
          servicer.getAvailableConfigs,
          request_deserializer=common__pb2.Request.FromString,
          response_serializer=transManager__pb2.configResponse.SerializeToString,
      ),
      'exportConfigs': grpc.unary_unary_rpc_method_handler(
          servicer.exportConfigs,
          request_deserializer=common__pb2.Request.FromString,
          response_serializer=common__pb2.commonResponse.SerializeToString,
      ),
      'getAvailableDatasets': grpc.unary_unary_rpc_method_handler(
          servicer.getAvailableDatasets,
          request_deserializer=common__pb2.Request.FromString,
          response_serializer=transManager__pb2.datasetResponse.SerializeToString,
      ),
      'getVolumeFromDataset': grpc.unary_stream_rpc_method_handler(
          servicer.getVolumeFromDataset,
          request_deserializer=common__pb2.Request.FromString,
          response_serializer=transManager__pb2.volumeResponse.SerializeToString,
      ),
      'Download': grpc.unary_stream_rpc_method_handler(
          servicer.Download,
          request_deserializer=common__pb2.Request.FromString,
          response_serializer=transManager__pb2.dcmImage.SerializeToString,
      ),
      'DownloadVolume': grpc.unary_stream_rpc_method_handler(
          servicer.DownloadVolume,
          request_deserializer=transManager__pb2.RequestWholeVolume.FromString,
          response_serializer=transManager__pb2.volumeWholeResponse.SerializeToString,
      ),
      'DownloadVolumeProcessed': grpc.unary_stream_rpc_method_handler(
          servicer.DownloadVolumeProcessed,
          request_deserializer=transManager__pb2.RequestWholeVolume.FromString,
          response_serializer=transManager__pb2.volumeWholeResponse.SerializeToString,
      ),
      'DownloadMasks': grpc.unary_stream_rpc_method_handler(
          servicer.DownloadMasks,
          request_deserializer=common__pb2.Request.FromString,
          response_serializer=transManager__pb2.dcmImage.SerializeToString,
      ),
      'DownloadMasksVolume': grpc.unary_stream_rpc_method_handler(
          servicer.DownloadMasksVolume,
          request_deserializer=common__pb2.Request.FromString,
          response_serializer=transManager__pb2.volumeWholeResponse.SerializeToString,
      ),
      'DownloadCenterLineData': grpc.unary_stream_rpc_method_handler(
          servicer.DownloadCenterLineData,
          request_deserializer=common__pb2.Request.FromString,
          response_serializer=transManager__pb2.centerlineData.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'helmsley.dataTransfer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
