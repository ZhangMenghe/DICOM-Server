from proto.transManager_pb2 import *
from proto.transManager_pb2_grpc import *
from proto.inspectorSync_pb2 import *
from proto.inspectorSync_pb2_grpc import *
from proto.common_pb2 import * 
from proto.common_pb2_grpc import *

from transUtils import *
import queue
from time import time
import threading

class operationServicer(inspectorSyncServicer):
    def __init__(self):
        self.provider = None
        self.ops = []
        self.gesture_pool = []
        self.tune_pool = []
        self.check_pool = []
        self.mask_value = None
        self.reset_value = None
        self.mtx = threading.Lock()
        self.current_data = None
        self.volume_info = None

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

    def reqestReset(self, msg, context):
        try:
            self.ops.remove(FrameUpdateMsg.MsgType.RESET)
        except:
            pass
        self.ops.append(FrameUpdateMsg.MsgType.RESET)
        self.reset_value = msg
        
    def setGestureOp(self, touch, context):
        self.ops.append(FrameUpdateMsg.MsgType.GESTURE)
        self.gesture_pool.append(touch) 

    def setTuneParams(self, tune, context):
        self.ops.append(FrameUpdateMsg.MsgType.TUNE)
        self.tune_pool.append(tune)

    def setCheckParams(self, check, context):
        self.ops.append(FrameUpdateMsg.MsgType.CHECK)
        self.check_pool.append(check)

    def setMaskParams(self, msk, context):
        try:
            self.ops.remove(FrameUpdateMsg.MsgType.MASK)
        except:
            pass
        self.ops.append(FrameUpdateMsg.MsgType.MASK)
        self.mask_value = msk
    def setDisplayVolume(self, msg, context):
        if(msg.vol_path == self.current_data):
            return
        try:
            self.ops.remove(FrameUpdateMsg.MsgType.DATA)
        except:
            pass
        self.ops.append(FrameUpdateMsg.MsgType.DATA)
        self.current_data = msg.vol_path
        self.volume_info = msg

    def getUpdates(self, req, context):
        # mutex.acquire()
        self.gesture_pool.sort(key = lambda x: int(x.gid))
        rt = FrameUpdateMsg(types = self.ops, gestures = self.gesture_pool, tunes = self.tune_pool, checks=self.check_pool, mask_value=self.mask_value, reset_value=self.reset_value, data_value=self.volume_info)
        self.ops = []
        self.gesture_pool = []
        self.tune_pool = []
        self.check_pool = []
        self.mask_value = None
        self.reset_value = None
        # mutex.release()
        return rt

    def getOperations(self, req, context):
        if(len(self.gesture_pool) == 0):
            return None
        self.gesture_pool.sort(key = lambda x: int(x.gid))
        ges_batch = OperationBatch(bid = time(), gesture_op = self.gesture_pool)
        self.gesture_pool.clear()
        return ges_batch

        # while not self.op_pool.empty():
        #     yield OperationResponse(gesture_op = self.op_pool.get())

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