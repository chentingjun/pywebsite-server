# -*- coding: utf-8 -*-
import json


CODEMSG = {
    'user': '301',  # 直接展示给用户
    'code': '201',  # 程序错误
    'res': '100',  # 正常返回
    'login': '-1'  # 需要用户重新登录
}


def get_result(code='res', result=None, msg=''):
    res = {'msg': msg, 'result': result, 'code': CODEMSG[code]}
    return json.dumps(res)
