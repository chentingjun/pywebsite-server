# -*- coding: utf-8 -*-
import pymysql
import re


class OpSql():
    _sqlconfig = {
        'host': 'localhost',
        'user': 'ctj',
        'password': '123456',
        'db': 'test_data_base'
    }

    def __init__(self, host=None, user=None, password=None, db=None):
        self._sqlconfig['host'] = host or self._sqlconfig['host']
        self._sqlconfig['user'] = user or self._sqlconfig['user']
        self._sqlconfig['password'] = password or self._sqlconfig['password']
        self._sqlconfig['db'] = db or self._sqlconfig['db']

    # 数据库操作-获取操作对象
    def getConCur(self):
        sqlconfig = self._sqlconfig
        con = pymysql.connect(host=sqlconfig['host'],
                              user=sqlconfig['user'],
                              password=sqlconfig['password'],
                              db=sqlconfig['db'])
        cur = con.cursor()
        return con, cur

    # 数据库操作-增
    def insertSql(self, sql, params=()):
        con, cur = self.getConCur()
        try:
            cur.execute(sql, params)
            con.commit()
        except Exception as e:
            con.rollback()
            raise
        finally:
            cur.close()
            con.close()

    # 数据库操作-删
    def deleteSql(self, sql, params=()):
        self.insertSql(sql, params)

    # 数据库操作-改
    def updateSql(self, sql, params=()):
        self.insertSql(sql, params)

    # 数据库操作-查
    def selectSql(self, sql, params=()):
        con, cur = self.getConCur()
        res = {'msg': 'success', 'result': ()}
        try:
            cur.execute(sql, params)
            res['result'] = cur.fetchall()
        except Exception as e:
            con.rollback()
            res['msg'] = e
        finally:
            cur.close()
            con.close()
        return res

if __name__ == "__main__":
    pass
