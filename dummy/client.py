import time
import grpc

import file_pb2_grpc
import file_pb2
from utils import get_file_chunks, save_chunks_to_file

SERVER_ADDRESS = "localhost:23333"
CLIENT_ID = 1

# 双向流模式 (在一次调用中, 客户端和服务器都可以向对方多次收发数据)
# stream-stream (In a single call, both client and server can send and receive data
# to each other multiple times.)
def bidirectional_streaming_method(stub):
    print(
        "--------------Call BidirectionalStreamingMethod Begin---------------")

    # 创建一个生成器
    # create a generator
    def request_messages():
        for i in range(5):
            request = file_pb2.Request(
                client_id=CLIENT_ID,
                request_data=("called by Python client, message: %d" % i))
            yield request
            time.sleep(1)

    response_iterator = stub.BidirectionalStreamingMethod(request_messages())
    for response in response_iterator:
        print("recv from server(%d), message=%s" % (response.server_id,
                                                    response.response_data))

    print("--------------Call BidirectionalStreamingMethod Over---------------")

class FileClient:
    def __init__(self, address):
        channel = grpc.insecure_channel(address)
        self.stub = file_pb2_grpc.fileChunkerStub(channel)

    def upload(self, in_file_name):
        chunks_generator = get_file_chunks(in_file_name)
        response = self.stub.upload(chunks_generator)
        print("server said...." + response.response_data)
        # assert response.length == os.path.getsize(in_file_name)

    def download(self, target_name, out_file_name):
        print("downloading " + target_name + " from server...")
        response = self.stub.download(file_pb2.Request(client_id=CLIENT_ID,request_data=target_name))
        
        print("saving (or use) ..." + out_file_name)
        save_chunks_to_file(response, out_file_name)

def main():
    client = FileClient(SERVER_ADDRESS)
    # uploading
    # client.upload('ct.txt')
    # downloading
    client.download('pizza-cat.jpg', 'test.jpg')



if __name__ == '__main__':
    main()
