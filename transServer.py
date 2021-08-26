from threading import Thread
from concurrent import futures

import grpc
import sys
#sys.path.insert(1, 'helmsley/')
from Servicer import *
 
class transServer():
    def __init__(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        self.data_servicer = dataServicer()
        self.op_servicer = operationServicer()
        add_dataTransferServicer_to_server(self.data_servicer, self.server)
        add_inspectorSyncServicer_to_server(self.op_servicer, self.server)
    
    def setup(self, pacs_dir, pacs_index_path, config_dir, port_num):
        self.port = '[::]:'+port_num
        self.data_servicer.setup(pacs_dir, pacs_index_path, config_dir)

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