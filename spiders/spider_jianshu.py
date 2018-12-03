import requests
from bs4 import BeautifulSoup
import re
from comm_functions import OpSql

opsql = OpSql()

selfheaders = {
    'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
url = 'https://www.jianshu.com/'

res = requests.get(url, headers=selfheaders)

soup = BeautifulSoup(res.text, 'lxml')

article_list = soup.find_all(id=re.compile(r'note-\d+'))

for article_item in article_list:
    article_id = article_item['data-note-id'].strip()
    img_wrapper = article_item.find(class_='wrap-img')
    img = img_wrapper.find(name='img') if img_wrapper else None
    img_src = img['src'] if img else ''
    title_ele = article_item.find(class_='title')
    title = title_ele.get_text().strip() if title_ele else ''
    abstract_ele = article_item.find(class_='abstract')
    abstract = abstract_ele.get_text().strip() if abstract_ele else ''
    nick_ele = article_item.find(class_='nickname')
    nickname = nick_ele.get_text().strip() if nick_ele else ''
    comment_ele = article_item.find(class_='ic-list-comments')
    comment_num = comment_ele.next_sibling.strip() if comment_ele else 0
    like_ele = article_item.find(class_='ic-list-like')
    like_num = like_ele.next_sibling.strip() if like_ele else 0
    opsql.insertSql('INSERT INTO article_jianshu (`title`, `article_id`, `abstract`, `nickname`, `img_src`, `comment_num`, `like_num`) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                    (title, article_id, abstract, nickname, img_src, comment_num, like_num))
    print('1')
