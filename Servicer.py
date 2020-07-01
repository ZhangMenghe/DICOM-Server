from proto.transManager_pb2 import *
from proto.transManager_pb2_grpc import *
from proto.inspectorSync_pb2 import *
from proto.inspectorSync_pb2_grpc import *
from proto.common_pb2 import * 
from proto.common_pb2_grpc import *

from transUtils import *
import queue

class operationServicer(inspectorSyncServicer):
    def __init__(self):
        self.provider = None
        self.op_pool = queue.Queue()
    def startBroadcast(self, info, context):
        if self.provider is not None:
            return commonResponse(success = False, res_msg = "exisiting broadcaster")
        self.provider = info.client_id

    def gsVolumePose(self, msg, context):
        # print("===Client" + str(msg.client_id) + )
        print(msg.req_type)
        print(msg.volume_pose_type)

        print(msg.values)

        return commonResponse(success = True, res_msg="lalalala")
    def setGestureOp(self, touch, context):
        self.op_pool.put(touch)
        # print(touch.type)
        # print(touch.x)
        # print(touch.y)
    def getOperations(self, req, context):
        while not self.op_pool.empty():
            yield OperationResponse(gesture_op = self.op_pool.get())

class dataServicer(dataTransferServicer):
    def __init__(self):
        pass
        # self.local_data_path = "data"
        # self.local_mask_path = "data_mask"
        # self.trans_manager = transDataManager(pacs_dir, self.local_data_path)

    def setup(self, pacs_dir, pacs_index_path, config_dir):
        self.trans_manager = transDataManager(pacs_dir,config_dir)
        self.pacs_index_path = pacs_index_path

    def getAvailableConfigs(self, request, context):
        print("===Client: " + str(request.client_id)+" Request config files===")
        return self.trans_manager.get_config_files()
    def exportConfigs(self, request, context):
        # request.req_msg
        print("===Client: " + str(request.client_id)+" export config files===")
        return self.trans_manager.export_config_file(request.req_msg)

    def getAvailableDatasets(self, request, context):
        print("===Client: " + str(request.client_id)+" Request all avaliable dataset of remote server===")
        return self.trans_manager.get_all_available_datasets(self.pacs_index_path)

    def getVolumeFromDataset(self, request, context):
        print("===Client: " + str(request.client_id)+" Request to browser all datas in %s ===" %request.req_msg)
        return self.trans_manager.getVolumeInfoListFromDS(request.req_msg, "index.txt")

    def Download(self, request, context):
        print("===Client: " + str(request.client_id)+" Download from .." + request.req_msg + " as images")
        return self.trans_manager.download_folder_as_images(request.req_msg)

    def DownloadVolume(self, request, context):
        print("===Client: " + str(request.client_id)+" Download from .." + request.req_msg + " as volume")
        return self.trans_manager.download_folder_as_volume(request.req_msg, request.unit_size)

    def DownloadMasks(self, request, context):
        print("===Client: " + str(request.client_id)+" Trying to return or inference Segmentation...")
        return self.trans_manager.inference_masks_as_images(request.req_msg)
    def DownloadMasksVolume(self, request, context):
        print("===Client: " + str(request.client_id)+" Stream Masks from " + request.req_msg)
        return self.trans_manager.inference_masks_as_volume(request.req_msg)