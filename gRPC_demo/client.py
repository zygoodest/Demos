#!/usr/bin/python3

import sys
import grpc

sys.path.append("./interface")

import test_pb2_grpc as s
import test_pb2 as msg

stub = None

class Client(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        """重写new方法，实现单例模式"""
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.grpc_host = "localhost:50051"          # grpc服务器地址
        self.timeout = 10                           # 等待服务器的超时时间(秒)
        self.channel = None                         # 与grpc服务器的通道
        self.stub = None                            # 客户端的stub对象
        self.respons = None                         # 响应体

        self.init_channel()
        self.init_server()

    def init_channel(self):
        """与服务器建立通道(不安全的通道)"""
        self.channel = grpc.insecure_channel(self.grpc_host)
        try:
            # 设定超时时间
            grpc.channel_ready_future(self.channel).result(timeout=self.timeout)
        except grpc.FutureTimeoutError:
            print("超时")
            sys.exit("Error connecting to server")

    def init_server(self):
        """实例化一个stub"""
        self.stub = s.TestStub(self.channel)
        global mystub
        mystub = self.stub

    def SayHello(self):
        request = msg.MyRequest(name="zy")
        response = self.stub.SayHello(request)
        print(response)



if __name__ == "__main__":
    c = Client()

    
    request1 = msg.MyRequest(name="zy")

    response1 = stub.UnaryRPCs(request1)
    print(response1.name)
    print("*******************************")


    response2 = stub.ServerStreamingRPCs(request1)
    for i in response2:
        print(i.name)
    print("*******************************")


    def mad_iterator():
        for i in range(5):
            tmp = msg.MyRequest(name=str(i))
            yield tmp

    response3 = stub.ClientStreamingRPCs(mad_iterator())
    print(response3)
    print("*******************************")


    response4 = stub.BidirectionalStreamingRPCs(mad_iterator())
    for i in response4:
        print(i.name)
    print("*******************************")





















