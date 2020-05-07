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
            
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        self.servicer = Servicer()
        add_dataTransferServicer_to_server(self.servicer, self.server)
        
    def setup(self, pacs_dir, pacs_index_path, config_dir, port_num):
        self.port = '[::]:'+port_num
        self.servicer.setup(pacs_dir, pacs_index_path, config_dir)

    def run(self):
        print("-----------start Python GRPC server-----------")
        self.server.add_insecure_port(self.port)
        self.server.start()
        self.server.wait_for_termination()

def main():
    args = parse_command()
    server = transServer()
    server.setup(args.pacs_dir, args.pacs_index_path, args.config_dir, args.port)
    server.run()


if __name__ == '__main__':
    main()