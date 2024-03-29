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
        self.receivers = {}

        self.ops = []
        self.gesture_pool = []
        self.tune_pool = []
        self.check_pool = []
        self.mask_value = None
        self.reset_value = None
        self.mtx = threading.Lock()
        # self.current_data = None
        self.data_info = None
        self.data_need_built = True

        self.frame_state = None
        self.last_time = None

        self.volume_pose_pool = []

    def startBroadcast(self, info, context):
        if self.provider is not None:
            self.receivers[self.provider] = False
            print("===id: " + str(self.provider) + " changed to receiver")
            self.receivers.pop(info.client_id, None)
        self.provider = info.client_id
        print("===id: " + str(self.provider) + " start to broadcast")
        #TODO: clear pools?
        return commonResponse(success = True)
    
    def startReceiveBroadcast(self, info, context):
        if self.provider == info.client_id:
            self.provider = None
        self.receivers[info.client_id] = False
        print("===id: " + str(info.client_id) + " register as receiver")
        return commonResponse(success = True)

    def check_host_client_status(self, nid, rtype=ReqType.SET):
        if(self.provider is None):
            return False

        if rtype == ReqType.SET:
            return self.provider == nid

        return nid in self.receivers.keys() and not self.receivers[nid]

    def setVolumePose(self, msg, context):
        if not self.check_host_client_status(msg.client_id):
            return commonResponse(success = False)
        self.volume_pose_pool.append(msg)
        return commonResponse(success = True)

    def requestReset(self, msg, context):
        if not self.check_host_client_status(msg.client_id):
            return commonResponse(success = False)
        try:
            self.ops.remove(FrameUpdateMsg.MsgType.RESET)
        except:
            pass
        self.ops.append(FrameUpdateMsg.MsgType.RESET)
        self.reset_value = msg
        return commonResponse(success = True)

    def setGestureOp(self, msg, context):
        if not self.check_host_client_status(msg.client_id):
            return commonResponse(success = False)
        self.ops.append(FrameUpdateMsg.MsgType.GESTURE)
        self.gesture_pool.append(msg)
        return commonResponse(success = True)

    def setTuneParams(self, msg, context):
        if not self.check_host_client_status(msg.client_id):
            return commonResponse(success = False)
        self.ops.append(FrameUpdateMsg.MsgType.TUNE)
        self.tune_pool.append(msg)
        return commonResponse(success = True)

    def setCheckParams(self, msg, context):
        if not self.check_host_client_status(msg.client_id):
            return commonResponse(success = False)
        self.ops.append(FrameUpdateMsg.MsgType.CHECK)
        self.check_pool.append(msg)
        return commonResponse(success = True)

    def setMaskParams(self, msg, context):
        if not self.check_host_client_status(msg.client_id):
            return commonResponse(success = False)
        try:
            self.ops.remove(FrameUpdateMsg.MsgType.MASK)
        except:
            pass
        self.ops.append(FrameUpdateMsg.MsgType.MASK)
        self.mask_value = msg
        return commonResponse(success = True)
    
    def setDisplayVolume(self, msg, context):
        if not self.check_host_client_status(msg.client_id):
            return commonResponse(success = False)
        # m_path_id = msg.ds_name + "/" + msg.volume_name
        # if(m_path_id == self.current_data):
        #     print("same data")
        #     return
        self.data_info = msg
        try:
            self.ops.remove(FrameUpdateMsg.MsgType.DATA)
        except:
            pass
        self.ops.append(FrameUpdateMsg.MsgType.DATA)
        print("====set data====" + msg.ds_name + " / "+ msg.volume_name)
        # self.current_data = m_path_id
        return commonResponse(success = True)

    def getUpdates(self, req, context):
        if not self.check_host_client_status(req.client_id, rtype=ReqType.GET):
            return FrameUpdateMsg(types=None)

        if self.data_need_built:
            self.gesture_pool.sort(key = lambda x: int(x.gid))
            if FrameUpdateMsg.MsgType.DATA in self.ops:
                if(self.data_info is not None):
                    print(self.data_info.ds_name)
                else:
                    print("msg is none")
            self.frame_state = FrameUpdateMsg(types = self.ops, gestures = self.gesture_pool, tunes = self.tune_pool, checks=self.check_pool, mask_value=self.mask_value, reset_value=self.reset_value, data_value=self.data_info)
            self.ops = []
            # if(data_need_updated and not data_info_updated):
            #     self.ops = [FrameUpdateMsg.MsgType.DATA]
            self.gesture_pool = []
            self.tune_pool = []
            self.check_pool = []
            self.mask_value = None
            self.reset_value = None
            self.data_info = None
            self.data_need_built = False
        self.receivers[req.client_id] = True
        # current_time = time()

        # if(self.last_time is None):
        #     self.last_time = current_time
        if(len(set(self.receivers.values())) == 1):#  or current_time - self.last_time > 30
        #     self.last_time = current_time
            for key, value in self.receivers.items():
                self.receivers[key] = False
            self.data_need_built = True
        return self.frame_state 

    def getOperations(self, req, context):
        if not self.check_host_client_status(req.client_id, rtype=ReqType.GET) or not self.gesture_pool :
            return OperationBatch(bid = time(), gesture_op = None)
        self.gesture_pool.sort(key = lambda x: int(x.gid))
        ges_batch = OperationBatch(bid = time(), gesture_op = self.gesture_pool)
        self.gesture_pool.clear()
        return ges_batch

        # while not self.op_pool.empty():
        #     yield OperationResponse(gesture_op = self.op_pool.get())
    
    def getVolumePoses(self, req, context):
        if not self.check_host_client_status(req.client_id, rtype=ReqType.GET) or not self.volume_pose_pool :
            return VolumePoseBatch(bid = time(), pose_msgs = None)
        self.volume_pose_pool.sort(key = lambda x: int(x.gid))
        pose_batch = VolumePoseBatch(bid = time(), pose_msgs = self.volume_pose_pool.copy())
        self.volume_pose_pool.clear()
        return pose_batch
    def getStatusMessage(self, req, context):
        return StatusMsg(host_id = self.provider)

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
    
    def DownloadVolumeProcessed(self, request, context):
        print("===Client: " + str(request.client_id)+" Download from Processed .." + request.req_msg + " as volume")
        return self.trans_manager.download_processed_as_volume(request.req_msg)

    def DownloadMasks(self, request, context):
        print("===Client: " + str(request.client_id)+" Trying to return or inference Segmentation...")
        return self.trans_manager.inference_masks_as_images(request.req_msg)
    def DownloadMasksVolume(self, request, context):
        print("===Client: " + str(request.client_id)+" Stream Masks from " + request.req_msg)
        return self.trans_manager.inference_masks_as_volume(request.req_msg)
    def DownloadCenterLineData(self, request, context):
        print("===Client: " + str(request.client_id) + " Start to send centerline data")
        return self.trans_manager.get_centerline(request.req_msg)