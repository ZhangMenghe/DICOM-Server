from threading import Thread
from concurrent import futures

import grpc
from transManager_pb2 import *
from transManager_pb2_grpc import *
from transUtils import *

class transServer(dataTransferServicer):
    def __init__(self):
        class Servicer(dataTransferServicer):
            def __init__(self):
                pass
                # self.local_data_path = "data"
                # self.local_mask_path = "data_mask"
                # self.trans_manager = transDataManager(pacs_dir, self.local_data_path)
            
            def setup(self, pacs_dir, pacs_mask_dir, pacs_index_path):
                self.trans_manager = transDataManager(pacs_dir)
                self.pacs_index_path = pacs_index_path
                self.pacs_mask_dir = pacs_mask_dir
            
            def getAvailableDatasets(self, request, context):
                print("===Request all avaliable dataset of remote server===")
                return self.trans_manager.get_all_available_datasets(self.pacs_index_path)
            
            def getVolumeFromDataset(self, request, context):
                print("===Request to browser all datas in %s ===" %request.req_msg)
                return self.trans_manager.get_all_available_volumes(request.req_msg)

            def Download(self, request, context):
                print("Download from .." + request.req_msg)
                return self.trans_manager.download_folder_as_stream(request.req_msg)

            def DownloadMasks(self, request, context):
                print("Trying to return or inference Segmentation...")
                return self.trans_manager.inference_masks_as_stream(self.pacs_mask_dir, request.req_msg)

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        self.servicer = Servicer()
        add_dataTransferServicer_to_server(self.servicer, self.server)
        
    def setup(self, pacs_dir, pacs_mask_dir, pacs_index_path, port_num):
        self.port = '[::]:'+port_num
        self.servicer.setup(pacs_dir, pacs_mask_dir, pacs_index_path)

    def run(self):
        print("-----------start Python GRPC server-----------")
        self.server.add_insecure_port(self.port)
        self.server.start()
        self.server.wait_for_termination()

def main():
    args = parse_command()
    server = transServer()
    server.setup(args.pacs_dir, args.pacs_mask_dir, args.pacs_index_path, args.port)
    server.run()


if __name__ == '__main__':
    main()