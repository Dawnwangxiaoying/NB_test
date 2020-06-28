# -*- coding: utf-8 -*-

"""
连接数据库

"""

import pymysql
from Conf.Config import Config



class Mysqlconnect:
    def __init__(self):
        conf = Config()
        self.host = conf.Mysqlhost
        self.port = conf.Mysqlport
        self.user = conf.Mysqluser
        self.passwd = conf.Mysqlpasswd


    def info(self, db, sel_sql):
        con = pymysql.Connect(host=self.host, port=int(self.port), db=db, user=self.user, passwd=self.passwd, charset='utf8')
        cursor = con.cursor()
        try:
            # 执行sql语句
            cursor.execute(sel_sql)
            msg = cursor.fetchall()
        except:
            # 发生错误时回滚
            db.rollback()
        con.close()
        return msg[0]

#
# sqlinfo = Mysqlconnect()
# info = sqlinfo.info('subscription','select * from prd_order')
# print(info[0])
