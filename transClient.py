import time
import grpc
import os

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'proto/')

from proto.transManager_pb2 import *
from proto.transManager_pb2_grpc import *
from proto.inspectorSync_pb2 import *
from proto.inspectorSync_pb2_grpc import *
from transUtils import *
from shutil import copyfile
from time import time

SERVER_ADDRESS = "localhost:23333"
CLIENT_ID = 100

class transClient:
    def __init__(self, address):
        channel = grpc.insecure_channel(address)
        self.stub = dataTransferStub(channel)
        self.syncer = inspectorSyncStub(channel)

        self.volume_pose_id = 0
    def setRST(self, type, value):
        res = self.syncer.setVolumePose(VPMsg(client_id = CLIENT_ID,gid=self.volume_pose_id, volume_pose_type= type, values = value))
        self.volume_pose_id+=1
        # print(res.res_msg)
    def getVolumePoses(self):
        res = self.syncer.getVolumePoses(Request(client_id = CLIENT_ID))
        if res.pose_msgs is not None:
            for it in res.pose_msgs:
                print(it)
    def getOperations(self):
        res = self.syncer.getOperations(Request(client_id = CLIENT_ID))
        if res.gesture_op is not None:
            for it in res.gesture_op:
                print(it.gesture_op.type)
    def getAvailableConfigs(self):
        ava_lst = self.stub.getAvailableConfigs(Request(client_id = CLIENT_ID))
        print(ava_lst)
        return ava_lst
    def getAvailableDatasets(self):
        ava_lst = self.stub.getAvailableDatasets(Request(client_id = CLIENT_ID))
        print(ava_lst)
        return ava_lst
        # vconfig = self.stub.getConfig(Request(client_id = CLIENT_ID, req_msg=folder_name))
        # print("returned configs: " + vconfig.folder_name + "nums: %d, width: %d" % (vconfig.file_nums, vconfig.img_width))
    def getAvailableVolume(self, folder_name):
        resp = self.stub.getVolumeFromDataset(Request(client_id=CLIENT_ID, req_msg=folder_name))
        ava_vols = []
        for it in resp:
            ava_vols.extend(it.volumes)
            # for v in it.volumes:
            #     print(v.folder_name)
            # print("=====")
        return ava_vols
    def download(self, folder_name):
        print("downloading from server...")
        response = self.stub.Download(Request(client_id=CLIENT_ID,req_msg=folder_name))

        # print("saving (or use) ..." + out_file_name)
        f = open('sample_data_4bytes', 'wb+')
        for it in response:
            print(it.position)
            f.write(it.data)
        f.close()

        # save_dcmImgs_to_file(response, out_file_name)
    def download_volume(self, folder_name):
        print("downloading from server...")
        response = self.stub.DownloadVolume(RequestWholeVolume(client_id=CLIENT_ID, req_msg=folder_name, unit_size = 2))

        # print("saving (or use) ..." + out_file_name)
        names = folder_name.split('/')
        
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        f = open(folder_name + '/'+'data', 'wb+')
        for it in response:
            f.write(it.data)
        f.close()
    def download_volume_processed(self, folder_name):
        print("downloading Processed from server...")
        response = self.stub.DownloadVolumeProcessed(RequestWholeVolume(client_id=CLIENT_ID, req_msg=folder_name))

        # print("saving (or use) ..." + out_file_name)
        names = folder_name.split('/')
        
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        f = open(folder_name + '/'+'data_processed', 'wb+')
        for it in response:
            f.write(it.data)
        f.close()
    def getMasks(self, folder_name):
        itrs = self.stub.DownloadMasks(Request(client_id = CLIENT_ID,req_msg=folder_name))
        
        for it in itrs:
            print(it.position)
            # np.save('sample/'+str(it.dcmID), it.data)
    def getMasks_volume(self, folder_name):
        itrs = self.stub.DownloadMasksVolume(Request(client_id = CLIENT_ID,req_msg=folder_name))
        names = folder_name.split('/')
        new_name = '/'.join(names[:-1]) + '/' +'_'.join(names[-1].split(' '))
        f = open(new_name + '/'+'mask', 'wb+')
        for it in itrs:
            it.data
            f.write(it.data)
        f.close()
    def getCenterLineData(self, folder_name):
        itrs = self.stub.DownloadCenterLineData(Request(client_id = CLIENT_ID,req_msg=folder_name))
        for it in itrs:
            print(it.data[0])
    

def main():
    client = transClient(SERVER_ADDRESS)
    while(True):
        client.getVolumePoses()
        client.getOperations()
    # client.setRST(VPMsg.VPType.POS, [1,2,3])
    # client.setRST(VPMsg.VPType.SCALE, [4,4,4])

    # ava_config = client.getAvailableConfigs()
    # ava_lst = client.getAvailableDatasets()
    # print(ava_lst)
    # dataset_name = ava_lst.datasets[0].folder_name
    # dataset_name = "IRB09"
    dataset_name = 'Larry_Smarr_2017'#"Larry_Smarr_2016"
    ava_vols = client.getAvailableVolume(dataset_name)
    for v in ava_vols:
        print(v.folder_name)
    
    # client.getMasks_volume('IRB09/' +'COR SSFSE')
    vol_name = dataset_name + "/"+ava_vols[0].folder_name

    vol_name = "IRB01/2100_FATPOSTCORLAVAFLEX20secs"
    print(vol_name)
    # vol_name = "Larry_Smarr_2016/series_23_Cor_LAVA_PRE-Amira"
    # vol_name = "IRB02/21_WATERPOSTCORLAVAFLEX20secs"
    # client.getCenterLineData(vol_name)
    # client.download_volume(vol_name)
    # client.download_volume_processed(vol_name)
    # client.getMasks_volume(vol_name)

    # vol_names = ["IRB01/2100_FATPOSTCORLAVAFLEX20secs","IRB02/21_WATERPOSTCORLAVAFLEX20secs","IRB03/22_WATERPOSTCORLAVAFLEX20secs","IRB04/21_WATERPOSTCORLAVAFLEX20secs", "IRB05/17_WATERPOSTCORLAVAFLEX20secs", "IRB06/19_WATERPOSTCORLAVAFLEX20secs"]
    # vol_names = ['IRB5/21_WATERPOSTCORLAVAFLEX20secs', 'IRB6/22_WATERPOSTCORLAVAFLEX20secs']
    # vol_names = ["IRB01/2100_FATPOSTCORLAVAFLEX20secs"]
    # vol_names = ["IRB03/22_WATERPOSTCORLAVAFLEX20secs"]#["IRB02/21_WATERPOSTCORLAVAFLEX20secs"]

    # for vol_name in vol_names:
    #     client.getCenterLineData(vol_name)
        # vol_path = '../data/PACS/' + vol_name
        # # os.makedirs(path.join(vol_path, "centerline"))
        # src_path = '../volume-rendering/app/src/main/assets/dicom-data/'+vol_name.split('/')[0]+'_normalized.txt'
        # print(src_path)
        # copyfile(src_path, path.join(vol_path, "centerline", "normalized.txt"))

        # client.download_volume(vol_name)
        # client.getMasks_volume(vol_name)



if __name__ == '__main__':
    main()
