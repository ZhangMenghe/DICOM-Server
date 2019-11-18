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
                self.request_path = None
            def getConfig(self, request, context):
                print("Request images in folder: " + request.req_msg)
                if not check_or_download_from_outside_server(REMOTE_ADDR, request.req_msg):
                    print("ERROR: Requested File Not exist")
                    return bundleConfig(file_nums = 0)
                self.request_path = request.req_msg    
                return parser_folder_config(request.req_msg)

            def Download(self, request, context):
                print("Download from .." + self.request_path)
                return download_folder_as_stream(self.request_path)

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_dataTransferServicer_to_server(Servicer(), self.server)
    
    def run(self, port):
        print("------------------start Python GRPC server")
        self.server.add_insecure_port(port)
        self.server.start()
        self.server.wait_for_termination()

def main():
    transServer().run(SERVER_ADDRESS)


if __name__ == '__main__':
    main()