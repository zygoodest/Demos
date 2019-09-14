from concurrent import futures
import time
import grpc

from mytype import users_pb2_grpc as users_service
from mytype import users_types_pb2 as users_messages

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class UsersService(users_service.UsersServicer):
    def CreateUser(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        user = users_messages.User(username=request.username, user_id=1)
        return users_messages.CreateUserResult(user=user)

    def GetUsers(self, request, context):
        for user in request.user:
            user = users_messages.User(
                username=user.username, user_id=user.user_id
            )
            yield users_messages.GetUsersResult(user=user)


class Server(object):
    def __init__(self):
        self.thread_sum = 10        # 线程数量
        self.server = None
        self.init_server()
        self.start()

    def init_server(self):
        thread_pool = futures.ThreadPoolExecutor(self.thread_sum)
        self.server = grpc.server(thread_pool)
        users_service.add_UsersServicer_to_server(UsersService(), self.server)
        self.server.add_insecure_port("127.0.0.1:50051")

    def start(self):
        print("开启grpc服务器")
        self.server.start()
        try:
            pass
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except:
            print("停止grpc服务器")
            self.server.stop(0)


if __name__ == "__main__":
    s = Server()
