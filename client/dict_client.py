"""
    dict_client
    查询字典的客户端框架
"""

from socket import *


class DictClient:
    def __init__(self, host, port):
        """
        根据传入的主机地址与端口号连接服务器
        :param host: 需要连接的服务器主机地址
        :param port: 需要连接的服务器主机端口号
        """
        self.__socket = socket(AF_INET, SOCK_STREAM)
        self.__host = host
        self.__port = port
        self.__address = (self.__host, self.__port)
        self.__connect()

    def __connect(self):
        self.__socket.connect(self.__address)

    # def run(self):
    #     self.__socket.send(b'Test')
    #     data = self.__socket.recv(1024).decode()
    #     print(data)
    #     self.__socket.close()

    def __generate_msg(self, cmd, **kwargs):
        data = cmd
        for key, value in kwargs.items():
            data += "#{key}:{value}".format(key=key, value=value)
        return data.encode()

    def register(self, name, passwd):
        send_msg = self.__generate_msg("register", name=name, passwd=passwd)
        self.__socket.send(send_msg)
        result = self.__socket.recv(1024)
        if result == b"ok":
            return True
        else:
            return False

    def login(self, name, passwd):
        send_msg = self.__generate_msg("login", name=name, passwd=passwd)
        self.__socket.send(send_msg)
        result = self.__socket.recv(1024)
        if result == b"ok":
            return True
        else:
            return False

    def exit(self):
        self.__socket.close()
