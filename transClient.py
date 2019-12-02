import time
import grpc
from transManager_pb2 import *
from transManager_pb2_grpc import *
from transUtils import *

SERVER_ADDRESS = "localhost:23333"
CLIENT_ID = 1

class transClient:
    def __init__(self, address):
        channel = grpc.insecure_channel(address)
        self.stub = dataTransferStub(channel)
    def getAvailableDatasets(self):
        ava_lst = self.stub.getAvailableDatasets(Request(client_id = CLIENT_ID))
        print(ava_lst)
        return ava_lst
        # vconfig = self.stub.getConfig(Request(client_id = CLIENT_ID, req_msg=folder_name))
        # print("returned configs: " + vconfig.folder_name + "nums: %d, width: %d" % (vconfig.file_nums, vconfig.img_width))
    def getAvailableVolume(self, folder_name):
        ava_vol = self.stub.getVolumeFromDataset(Request(client_id=CLIENT_ID,req_msg=folder_name))
        print(ava_vol)
        return ava_vol
    def download(self, folder_name):
        print("downloading from server...")
        response = self.stub.Download(Request(client_id=CLIENT_ID,req_msg=folder_name))

        # print("saving (or use) ..." + out_file_name)
        for it in response:
            print(it.position)
        # save_dcmImgs_to_file(response, out_file_name)
    def getMasks(self, folder_name):
        print("====masks")
        itrs = self.stub.DownloadMasks(Request(client_id = CLIENT_ID,req_msg=folder_name))
        for it in itrs:
            print(it.position)

def main():
    client = transClient(SERVER_ADDRESS)
    ava_lst = client.getAvailableDatasets()
    dataset_name = ava_lst.datasets[2].folder_name
    vol_lst = client.getAvailableVolume(dataset_name)
    vol_name = dataset_name + "/"+vol_lst.volumes[0].folder_name
    client.download(vol_name)
    client.getMasks(vol_name)



if __name__ == '__main__':
    main()
