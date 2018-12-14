import hashlib
import random
import string


def ToMd5(ori_str):  # MD5加密
    return hashlib.md5(ori_str.encode(encoding='UTF-8')).hexdigest()


def randomStr(num): # 随机串
    temp_str = string.ascii_letters + string.digits
    return ''.join([random.choice(temp_str) for i in range(num)])
