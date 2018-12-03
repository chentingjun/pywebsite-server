# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

import sys
import os

path = os.path.abspath('./') + '/mysqldb'
sys.path.append(path)

from comm_functions import OpSql

opsql = OpSql()

headers = {
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
r = requests.get('http://www.qiushibaike.com', {'headers': headers})
content = r.text
soup = BeautifulSoup(r.text, 'lxml')

divs = soup.find_all(class_='article block untagged mb15 typs_hot')

for div in divs:
    # title = div.find_all(class_='author')
    title = re.sub(r'\n', '', div.h2.get_text())
    joke = re.sub(r'\n', '', div.span.get_text())
    opsql.insertSql(
        'INSERT INTO article_spider (`article_name`, `article_txt`) VALUES (%s, %s)', (title, joke))
    print('【%s】\n %s' % (title, joke))
    print('------')


header = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    "host": "dxxxxxxxxxx.cn",
    "pragma": "no-cache",
    "referer": "http://xxxxxxxxxx.cn/login.htm",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
}


{
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN, zh q = 0.9, en q = 0.8",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    "Content-Length":"44",
    "Content-Type":"application/json charset = UTF-8",
    "Cookie":"beegosessionID = 82bb233428245a9bd267cfa1ad021612",
    "Host":"op3t.jingdaka.com",
    "Pragma":"no-cache",
    "User-Agent":"Mozilla/5.0 (Macintosh Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
}

{
    ('seen_snote_ids[]', '34827759'),
    ('seen_snote_ids[]', '32932258'),
    ('seen_snote_ids[]', '33598969'),
    ('seen_snote_ids[]', '35387300'),
    ('seen_snote_ids[]', '33238260'),
    ('seen_snote_ids[]', '36469691'),
    ('seen_snote_ids[]', '34733025'),
    ('page', '2'),
}
