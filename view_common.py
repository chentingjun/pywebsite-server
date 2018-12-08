from flask import request, session
import json
from mysqldb.operate_sql import OpSql
from utils import ToMd5

from response.code import get_result

op_sql = OpSql()


def login():
    if request.method != 'POST':
        return get_result(msg='错误的请求方式', code='code')
    data = request.data.decode('utf-8')
    params = json.loads(data)
    user_name = params.get('user_name', '')
    pwd_md5 = params.get('user_password', '')
    sqlRes = op_sql.selectSql(
        'SELECT * FROM user_info WHERE user_name = %s', user_name)
    select_arr = sqlRes.get('result', [])
    if len(select_arr) > 0:
        user_info = select_arr[0]
        user_pwd_md5 = ToMd5(user_info.get('user_password', ''))
        if user_pwd_md5 == pwd_md5:
            # session['user_name'] = user_info
            return get_result(result=user_info)
        else:
            return get_result(msg='密码错误', code='user')
    else:
        return get_result(msg='用户名错误', code='user')


def registe():
    if request.method != 'POST':
        return get_result(msg='错误的请求方式', code='code')
    data = request.data.decode('utf-8')
    params = json.loads(data)
    user_name = params.get('user_name', '')
    user_pwd = params.get('user_password', '')
    desc = params.get('desc', '')
    if user_name == '':
        return get_result(msg='用户名不能为空', code='user')
    if user_pwd == '':
        return get_result(msg='密码不能为空', code='user')
    select_res = op_sql.selectSql(
        'SELECT * FROM user_info WHERE user_name = %s', user_name)
    if len(select_res['result']) > 0:
        return get_result(msg='用户名已存在', code='user')
    insert_res = op_sql.insertSql(
        '''
            INSERT INTO user_info (`user_name`, `user_password`, `desc`)
            VALUES (%s, %s, %s)
        ''',
        (user_name, user_pwd, desc)
    )
    return get_result(msg=insert_res.get('msg', '缺少返回状态信息'), code='res')


def add_common_routes(app):
    app.add_url_rule('/api/login',
                     view_func=login, methods=['POST'])
    app.add_url_rule('/api/registe',
                     view_func=registe, methods=['POST'])


if __name__ == "__main__":
    res = registe()
    print(res)
