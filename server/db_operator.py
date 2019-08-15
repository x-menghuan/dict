"""
    db_operator.py
    数据库操作类
"""
import pymysql


class DBOperator:
    def __init__(self, host, port, user, passwd, database):
        self.__db = pymysql.connect(host=host,
                                    port=port,
                                    user=user,
                                    passwd=passwd,
                                    database=database)

        self.__cur = self.__db.cursor()

    def close(self):
        self.__cur.close()
        self.__db.close()

    def insert(self, table_name, **kwargs):
        """
        添加数据操作
        :param table_name:需要增加到的表名
        :param kwargs: 以列名与数据组成的键值对 组成字典传入
        :return: 返回添加成功的个数
        """
        keys = "(" + ",".join(kwargs.keys()) + ")"
        values = "(" + ",".join(['%s' for i in kwargs]) + ")"
        sql = "insert into %s %s values %s" % (table_name, keys, values)
        try:
            ret = self.__cur.execute(sql, tuple(kwargs.values()))
            self.__db.commit()
            return ret
        except Exception as e:
            print(e)
            self.__db.rollback()
            return None

    def query(self, table_name, condition, count=0):
        """
        数据查询操作
        :param table_name: 需要查询操作的表名
        :param condition: 查询的条件 sql字符串where以后的语句,不包含where和limit
        :param count: 需要查询的个数, 默认0代表查询全部
        :return: 返回查询的结果
        """
        if count == 0:
            sql = "select * from %s where %s" % (table_name, condition)
        else:
            sql = "select * from %s where %s limit %d" % (table_name, condition, count)
        try:
            self.__cur.execute(sql)
            return self.__cur.fetchall()
        except Exception as e:
            print(e)

    # def update(self):
    #     pass
    #
    # def delete(self):
    #     pass
