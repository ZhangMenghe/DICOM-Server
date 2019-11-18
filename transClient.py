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
    def getClient(self, folder_name):
        vconfig = self.stub.getConfig(Request(client_id = CLIENT_ID, req_msg=folder_name))
        print("returned configs: " + vconfig.folder_name + "nums: %d, width: %d" % (vconfig.file_nums, vconfig.img_width))
    def download(self, out_file_name):
        print("downloading from server...")
        response = self.stub.Download(Request(client_id=CLIENT_ID))

        print("saving (or use) ..." + out_file_name)
        save_dcmImgs_to_file(response, out_file_name)

def main():
    client = transClient(SERVER_ADDRESS)

    client.getClient("dicom_sample")
    client.download("bunnmmmy")



if __name__ == '__main__':
    main()
