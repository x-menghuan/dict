"""
    client_view.py
    客户端显示层
"""

import getpass
import re


class ClientView:
    def __init__(self, client):
        self.__client = client
        self.__is_running = True
        self.__is_login = False

    def run(self):
        while self.__is_running:
            self.__show_menu()

    def __show_menu(self):
        print("""
        ***********欢迎进入查询字典系统***********
                        1.注册
                        2.登录
                        3.退出
        ******************************************
        """)
        select = input("请输入:")
        if select == '1':
            self.__register()
        elif select == '2':
            self.__login()
        elif select == '3':
            self.__exit()
        else:
            print("输入有误")

    def __register(self):
        while True:
            name = input("请输入用户名:")
            if re.findall(r"[^_a-zA-Z0-9]", name) or len(name) > 20:
                print("用户名必须由字母数字与下划线组成,且长度必须在20个字符内")
                continue
            passwd = getpass.getpass("请输入密码:")
            if re.findall(r"[^_a-zA-Z0-9]", passwd) or not 6 <= len(passwd) <= 15:
                print("密码必须由字母数字与下划线组成,且长度必须是6-15个字符")
                continue
            passwd1 = getpass.getpass("请再输入一次密码:")
            if passwd != passwd1:
                print("两次密码不一致")
                continue
            ret = self.__client.register(name, passwd)
            if ret:
                print("注册成功")
                break
            else:
                res = input("注册失败,是否重新注册(y/n)?")
                if res != 'y':
                    break

    def __login(self):
        while True:
            name = input("请输入用户名:")
            if re.findall(r"[^_a-zA-Z0-9]", name) or len(name) > 20:
                print("用户名必须由字母数字与下划线组成,且长度必须在20个字符内")
                continue
            passwd = getpass.getpass("请输入密码:")
            if re.findall(r"[^_a-zA-Z0-9]", passwd) or not 6 <= len(passwd) <= 15:
                print("密码必须由字母数字与下划线组成,且长度必须是6-15个字符")
                continue
            ret = self.__client.login(name, passwd)
            if ret:
                print("登录成功")
                break
            else:
                res = input("登录失败,是否重新登录(y/n)?")
                if res != 'y':
                    break

    def __exit(self):
        print("谢谢使用")
        self.__is_running = False
        self.__client.exit()
