from threading import Thread
from concurrent import futures

import grpc
from transManager_pb2 import *
from transManager_pb2_grpc import *
from transUtils import *

SERVER_ADDRESS = '[::]:23333'
SERVER_ID = 1
REMOTE_ADDR = "/home/menghe/Github/data"

class transServer(dataTransferServicer):
    def __init__(self):
        class Servicer(dataTransferServicer):
            def __init__(self):
                self.local_data_path = "data"
                self.local_mask_path = "data_mask"
                self.trans_manager = transDataManager(REMOTE_ADDR, self.local_data_path)
            
            def getAvailableDatasets(self, request, context):
                print("===Request all avaliable dataset of remote server===")
                return self.trans_manager.get_all_available_datasets()
            
            def getVolumeFromDataset(self, request, context):
                print("===Request to browser all datas in %s ===" %request.req_msg)
                return self.trans_manager.get_all_available_volumes(request.req_msg)

            def Download(self, request, context):
                print("Download from .." + request.req_msg)
                return self.trans_manager.download_folder_as_stream(request.req_msg)
            def DownloadMasks(self, request, context):
                print("Trying to return or inference Segmentation...")
                return self.trans_manager.inference_masks_as_stream(self.local_mask_path, request.req_msg)

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_dataTransferServicer_to_server(Servicer(), self.server)
    
    def run(self, port):
        print("-----------start Python GRPC server-----------")
        self.server.add_insecure_port(port)
        self.server.start()
        self.server.wait_for_termination()

def main():
    transServer().run(SERVER_ADDRESS)


if __name__ == '__main__':
    main()