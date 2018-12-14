# -*- coding: utf-8 -*-
import pymysql
import re
import datetime


class OpSql():
    _sqlconfig = {
        'host': 'localhost',
        'port': 3306,
        'user': 'ctj',
        'passwd': '123456',
        'db': 'test_data_base'
        # 'host': '106.14.194.171',
        # 'user': 'jdkopen',
        # 'passwd': 'root',
        # 'db': 'XZhenzhuangtodb'
    }

    def __init__(self, host=None, port=None, user=None, passwd=None, db=None):
        self._sqlconfig['host'] = host or self._sqlconfig['host']
        self._sqlconfig['port'] = port or self._sqlconfig['port']
        self._sqlconfig['user'] = user or self._sqlconfig['user']
        self._sqlconfig['passwd'] = passwd or self._sqlconfig['passwd']
        self._sqlconfig['db'] = db or self._sqlconfig['db']

    # 数据库操作-获取操作对象
    def getConCur(self):
        sqlconfig = self._sqlconfig
        print(sqlconfig)
        try:
            con = pymysql.connect(host=sqlconfig['host'],
                                  user=sqlconfig['user'],
                                  port=sqlconfig['port'],
                                  passwd=sqlconfig['passwd'],
                                  db=sqlconfig['db'])
            cur = con.cursor()
            return con, cur
        except Exception as e:
            print('expression', e)
            return e, e

    # 数据库操作-增
    def insertSql(self, sql, params=()):
        res = {'msg': 'success', 'result': None}
        con, cur = self.getConCur()
        try:
            cur.execute(sql, params)
            con.commit()
        except Exception as e:
            con.rollback()
            res['result'] = e
            raise
        finally:
            cur.close()
            con.close()
            return res

    # 数据库操作-删
    def deleteSql(self, sql, params=()):
        return self.insertSql(sql, params)

    # 数据库操作-改
    def updateSql(self, sql, params=()):
        return self.insertSql(sql, params)

    # 数据库操作-查
    def selectSql(self, sql, params=()):
        con, cur = self.getConCur()
        result = []
        res = {'msg': 'success', 'result': []}
        try:
            cur.execute(sql, params)
            keys = cur.description
            for rowItem in cur.fetchall():
                row = {}
                for index in range(len(keys)):
                    if keys[index][0] == 'create_time':
                        t = rowItem[index].strftime(
                            '%Y-%m-%d %H:%M:%S')
                        print(t)
                        row[keys[index][0]] = t
                    else:
                        row[keys[index][0]] = rowItem[index]
                result.append(row)
        except Exception as e:
            con.rollback()
            res['msg'] = e
        finally:
            cur.close()
            con.close()
            res['result'] = result
        return res


if __name__ == "__main__":
    sql = OpSql()
    con, cur = sql.getConCur()
    print(con, cur)
    pass
