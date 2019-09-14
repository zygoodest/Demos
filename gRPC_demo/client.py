import sys

import grpc

from mytype import users_pb2_grpc as users_service
from mytype import users_types_pb2 as users_messages

class Client(object):
    def __init__(self):
        self.metadata = [('ip', '127.0.0.1')]
        self.grpc_host = "localhost:50051"          # grpc服务器地址
        self.timeout = 10                           # 设定等待服务返回的超时时间(单位秒)
        self.channel = None                         # 与grpc服务器的通道
        self.s = None                               # 实例化的服务
        self.response = None                        # 响应体

        self.init_channel()
        self.init_server()

    def init_channel(self):
        """与服务器建立通道(不安全通道)"""
        self.channel = grpc.insecure_channel(self.grpc_host)
        try:
            # 设定超时时间
            grpc.channel_ready_future(self.channel).result(timeout=self.timeout)
        except grpc.FutureTimeoutError:
            print("超时")
            sys.exit("Error connecting to server")

    def init_server(self):
        """实例化一个服务"""
        self.s = users_service.UsersStub(self.channel)

    def CreateUser(self, username):
        self.response = self.s.CreateUser(
            users_messages.CreateUserRequest(username=username),
            metadata = self.metadata
        )
        if self.response:
            print("User created:", self.response.user.username)

    def GetUsers(self):
        request = users_messages.GetUsersRequest(
            user=[users_messages.User(username="alexa", user_id=1),
                  users_messages.User(username="christie", user_id=1)]
        )
        response = self.s.GetUsers(request, timeout=0.00001)
        for i in response:
            print(i)


if __name__ == "__main__":
    c = Client()
    c.CreateUser("zy")
