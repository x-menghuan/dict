# 电子字典

## 数据库结构
> database: dict

>> * table: words
>>> * id
>>> * word
>>> * mean
 
>> * table: user
>>> * id
>>> * name
>>> * passwd

>> * table: history
>>> * id
>>> * name
>>> * word
>>> * time

## 服务端

> dict_server.py
>> * 利用线程实现tcp服务器的并发
>> * 处理客户端传来的数据并回馈相应数据

> db_operator.py
>> * 数据库封装类
>> * 实现数据库的连接/读/写操作

## 客户端

> dict_client.py
>> * 界面控制层
>> * 负责网络传输

> client_view.py
>> * 显示层
>> * 负责输入/输出