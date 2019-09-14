import threading

class Singleton():
    __lock = threading.Lock()
    __instance = None

    def __new__(cls, *args, **kwargs):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
                print("have a instance")
        return cls.__instance

    def __init__(self, name):
        self.name = name

a = Singleton("aa")
b = Singleton("bb")
c = Singleton("cc")


print(c.name)

