import time
import grpc
from pprint import pprint
from concurrent import futures

from interface import interface_pb2_grpc as service
from interface import interface_pb2 as messages

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


# 定义服务接口
class ServiceInterface(service.TestService):
    def send_msg(self, request, context):
        pprint(request)




# 编写服务器
class Server(object):
    def __init__(self):
        self.thread_sum = 10    # 开启线程数量
        self.server = None
        self.init_server()
        self.start()

    def init_server(self):
        thread_pool = futures.ThreadPoolExecutor(self.thread_sum)
        self.server = grpc.server(thread_pool)
        service.add_TestServer_to_server(ServiceInterface(), self.server)
        self.server.add_insecure_port("0.0.0.0:50051")

    def start(self):
        print("开启grpc服务器")
        self.server.start()
        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except:
            print("停止grpc服务器")
            self.server.stop(0)


if __name__ == "__main__":
    s = Server()


