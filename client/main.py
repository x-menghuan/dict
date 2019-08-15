"""
    客户端入口
"""

from dict_client import DictClient
from client_view import ClientView

HOST = "127.0.0.1"
PORT = 8888


def main():
    client = DictClient(HOST, PORT)
    view = ClientView(client)
    view.run()


if __name__ == '__main__':
    main()
