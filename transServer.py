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
                self.request_folder = None
                self.local_data_path = "data"
                self.local_mask_path = "data_mask"
                self.trans_manager = transDataManager()
            def getAvailableDatasetInfos(self, request, context):
                print("===Request all avaliable dataset of remote server===")
                return get_all_available_datasets(REMOTE_ADDR)

            def getConfig(self, request, context):
                print("Request images in folder: " + request.req_msg)
                if not check_or_download_from_outside_server(REMOTE_ADDR, self.local_data_path, request.req_msg):
                    print("ERROR: Requested File Not exist")
                    return bundleConfig(file_nums = 0)
                self.request_folder = request.req_msg
                print("=====???")  
                return parser_folder_config(self.local_data_path, request.req_msg)

            def Download(self, request, context):
                print("Download from .." + self.request_folder)
                return self.trans_manager.download_folder_as_stream(self.local_data_path, self.request_folder)
                # return download_folder_as_stream(self.local_data_path, self.request_folder)
            def getMasks(self, request, context):
                print("Trying to return or inference Segmentation...")
                return inference_masks_as_stream(self.local_mask_path, self.request_folder)

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