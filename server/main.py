"""
    服务器入口
"""
from dict_server import DictServer
from db_operator import DBOperator

HOST = '0.0.0.0'
PORT = 8888


def main():
    db = DBOperator('localhost', 3306, 'root', '123456', 'dict')
    server = DictServer(db, HOST, PORT)
    server.server_forever()
    db.close()


if __name__ == '__main__':
    main()
