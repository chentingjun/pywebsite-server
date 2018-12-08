import hashlib


def ToMd5(ori_str):  # MD5加密
    return hashlib.md5(ori_str.encode(encoding='UTF-8')).hexdigest()


def Hello():
  return 'hello'
