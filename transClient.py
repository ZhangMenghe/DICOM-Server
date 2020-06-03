import time
import grpc
import os

from transManager_pb2 import *
from transManager_pb2_grpc import *
from transUtils import *

SERVER_ADDRESS = "localhost:23333"
CLIENT_ID = 100

class transClient:
    def __init__(self, address):
        channel = grpc.insecure_channel(address)
        self.stub = dataTransferStub(channel)
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

    def getMasks(self, folder_name):
        print("====masks")
        itrs = self.stub.DownloadMasks(Request(client_id = CLIENT_ID,req_msg=folder_name))
        
        for it in itrs:
            print(it.position)
            # np.save('sample/'+str(it.dcmID), it.data)
    def getMasks_volume(self, folder_name):
        itrs = self.stub.DownloadMasksVolume(Request(client_id = CLIENT_ID,req_msg=folder_name))
        names = folder_name.split('/')
        f = open(folder_name + '/'+'mask', 'wb+')
        for it in itrs:
            f.write(it.data)
        f.close()

def main():
    client = transClient(SERVER_ADDRESS)
    # ava_config = client.getAvailableConfigs()
    # ava_lst = client.getAvailableDatasets()
    
    # dataset_name = ava_lst.datasets[3].folder_name
    dataset_name = "Larry_Smarr_2016"
    ava_vols = client.getAvailableVolume(dataset_name)
    for v in ava_vols:
        print(v)
    # vol_name = dataset_name + "/"+vol_lst.volumes[0].folder_name
    # print(vol_name)
    # vol_name = "Larry_Smarr_2017/Larry_2017"
    # client.download(vol_name)
    # client.getMasks(vol_name)
    # vol_names = ["IRB1/26_LAVACORPOST2", "IRB2/28_WATERPOSTCorLAVAFLEX2MM", "IRB3/2100_FATPOSTCORLAVAFLEX20secs", "IRB4/21_WATERPOSTCORLAVAFLEX20secs"]
    # vol_names = ['IRB5/21_WATERPOSTCORLAVAFLEX20secs', 'IRB6/22_WATERPOSTCORLAVAFLEX20secs']
    # vol_names = ["IRB1/26_LAVACORPOST2"]
    # for vol_name in vol_names:
    #     client.download_volume(vol_name)
    #     client.getMasks_volume(vol_name)



if __name__ == '__main__':
    main()
