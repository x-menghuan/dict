"""
    dict_server.py
    查询字典的服务器框架
"""

from socket import *
from threading import Thread
import hashlib


class DictServer:
    def __init__(self, db_operator, host="0.0.0.0", port=8888):
        """
        根据传入的主机地址与端口号创建服务器, 需要调用server_forever完成服务器的搭建
        :param host: 服务器监听的主机地址 默认监听"0.0.0.0"
        :param port: 服务器监听的主机端口号 默认监听8888
        """
        self.__socket = socket(AF_INET, SOCK_STREAM)
        self.__socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
        self.__host = host
        self.__port = port
        self.__address = (self.__host, self.__port)
        self.__bind()

        self.__db_operator = db_operator

    def __bind(self):
        self.__socket.bind(self.__address)
        self.__socket.listen(3)
        print("Listen port", self.__port)

    def server_forever(self):
        while True:
            try:
                connfd, addr = self.__socket.accept()
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(e)
                continue

            print("Connect from", addr)
            t = Thread(target=self.__handle, args=(connfd,))
            t.setDaemon(True)
            t.start()

    def __parse_msg(self, msg):
        # register#name:abc#passwd:123456
        list_msg = msg.split("#")
        cmd = list_msg[0]
        kwargs = {}
        for sub_msg in list_msg[1:]:
            key, value = sub_msg.split(":", 1)
            kwargs[key] = value
        return cmd, kwargs

    def __handle(self, connfd):
        while True:
            data = connfd.recv(1024).decode()
            if not data:
                break
            cmd, kwargs = self.__parse_msg(data)
            if cmd == "register":
                self.__register(connfd, **kwargs)
            elif cmd == "login":
                self.__login(connfd, **kwargs)
        connfd.close()

    def __register(self, connfd, name, passwd):
        if self.__db_operator.query("user", "name='%s'" % name):
            connfd.send(b'fail')
            return

        ret = self.__db_operator.insert("user", name=name, passwd=self.__encryption_passwd(passwd))
        if ret:
            connfd.send(b'ok')
        else:
            connfd.send(b'fail')

    def __login(self, connfd, name, passwd):
        ret = self.__db_operator.query("user", "name='%s' and passwd='%s'" % (name, self.__encryption_passwd(passwd)))
        if ret:
            connfd.send(b'ok')
        else:
            connfd.send(b'fail')

    def __encryption_passwd(self, passwd):
        hash = hashlib.md5(b"%g#o")
        hash.update(passwd.encode())
        return hash.hexdigest()
