#!/usr/bin/python3

import sys
import time
import grpc
from concurrent import futures

sys.path.append("./interface")

import test_pb2_grpc as s
import test_pb2 as msg

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Test(s.TestServicer):
    def SayHello(self, request, context):
        print(context)
        return msg.MyReply(name="aaa")




# 编写服务器
class Server(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.thread_sum = 50        # 线程池的大小
        self.server = None
        self.init_server()
        self.start()

    def init_server(self):
        thread_pool = futures.ThreadPoolExecutor(self.thread_sum)
        self.server = grpc.server(thread_pool)
        s.add_TestServicer_to_server(Test(), self.server)
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
