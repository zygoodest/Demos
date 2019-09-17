#!/usr/bin/python3

import sys
import time
import grpc
from concurrent import futures

sys.path.append("./interface")

import test_pb2_grpc as s
import test_pb2 as msg

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


# 实现一个派生类，重写rpc中的接口函数
class Test(s.TestServicer):

    def UnaryRPCs(self, request, context):
        print("收到一元RCP请求：" + request.name)
        return msg.MyReply(name="ok")

    def ServerStreamingRPCs(self, request, context):
        print("收到服务端流式RPC请求：" + request.name)
        li = ["11", "22", "33", "44", "55"]
        for i in li:
            yield msg.MyReply(name=i)

    def ClientStreamingRPCs(self, request, context):
        print("收到客户端流式RPC请求：")
        for i in request:
            print(i.name)
        return msg.MyReply(name="ok")

    def BidirectionalStreamingRPCs(self, request, context):
        print("收到双向流式RPC请求：")
        for i in request:
            print(i.name)
        li = ["11", "22", "33", "44", "55"]
        for i in li:
            yield msg.MyReply(name=i)





# 编写服务器
class Server(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        """重写new方法，实现单例模式"""
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.thread_sum = 50        # 线程池的大小
        self.server = None
        self.init_server()
        self.start()

    def init_server(self):
        thread_pool = futures.ThreadPoolExecutor(self.thread_sum)   # 创建线程池
        self.server = grpc.server(thread_pool)                      # 创建一个服务器
        s.add_TestServicer_to_server(Test(), self.server)           # 添加实现了的接口
        self.server.add_insecure_port("0.0.0.0:50051")              # 添加监听端口

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
