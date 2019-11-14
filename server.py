from threading import Thread
from concurrent import futures

import grpc
import file_pb2_grpc
import file_pb2
from utils import get_file_chunks, save_chunks_to_file

SERVER_ADDRESS = 'localhost:23333'
SERVER_ID = 1

class DemoServer(file_pb2_grpc.fileChunkerServicer):
    # stream-stream (In a single call, both client and server can send and receive data
    # to each other multiple times.)
    def BidirectionalStreamingMethod(self, request_iterator, context):
        print("BidirectionalStreamingMethod called by client...")

        # 开启一个子线程去接收数据
        # Open a sub thread to receive data
        def parse_request():
            for request in request_iterator:
                print("recv from client(%d), message= %s" %
                      (request.client_id, request.request_data))

        t = Thread(target=parse_request)
        t.start()

        for i in range(5):
            yield file_pb2.Response(
                server_id=SERVER_ID,
                response_data=("send by Python server, message= %d" % i))

        t.join()

class FileServer(file_pb2_grpc.fileChunkerServicer):
    def __init__(self):
        class Servicer(file_pb2_grpc.fileChunkerServicer):
            def __init__(self):
                self.file_name='test_save.txt'
            def upload(self, request_iterator, context):
                print("Tring to upload to server from client...")
                save_chunks_to_file(request_iterator, self.file_name)
                return file_pb2.Response(
                    server_id=SERVER_ID,
                    response_data=("finish uploading")
                )    
            def download(self, request, context):
                print("====request name " + request.request_data)
                if(request.request_data):
                    return get_file_chunks(request.request_data)
                else:
                    return get_file_chunks(self.file_name)      
        self.server = grpc.server(futures.ThreadPoolExecutor())
        file_pb2_grpc.add_fileChunkerServicer_to_server(Servicer(), self.server)
    
    def run(self, port):
        print("------------------start Python GRPC server")
        self.server.add_insecure_port(port)
        self.server.start()
        self.server.wait_for_termination()
def main():
   FileServer().run(SERVER_ADDRESS)


if __name__ == '__main__':
    main()
