import requests
from bs4 import BeautifulSoup
import re
from urllib import parse


class JianShuInfo ():
    selfheaders = {
        'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'x-infinitescroll': 'true'
    }
    listurl = 'https://www.jianshu.com'
    detailurl = 'https://www.jianshu.com/p/'

    def __init__(self):
        self.selfheaders = {
            'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
            'x-infinitescroll': 'true'
        }

    def searchList(self, page=1, params=''):
        res = requests.get(self.listurl, headers=self.selfheaders)
        soup = BeautifulSoup(res.text, 'lxml')
        article_list = soup.find_all(id=re.compile(r'note-\d+'))
        result = []
        for article_item in article_list:
            article_info = {}
            article_info['article_id'] = article_item['data-note-id'].strip()
            img_wrapper = article_item.find(class_='wrap-img')
            article_info['link'] = img_wrapper.attrs['href'] if img_wrapper and img_wrapper.name == 'a' else ''
            img = img_wrapper.find(name='img') if img_wrapper else None
            article_info['img_src'] = img['src'] if img else ''
            title_ele = article_item.find(class_='title')
            article_info['title'] = title_ele.get_text(
            ).strip() if title_ele else ''
            abstract_ele = article_item.find(class_='abstract')
            article_info['abstract'] = abstract_ele.get_text(
            ).strip() if abstract_ele else ''
            nick_ele = article_item.find(class_='nickname')
            article_info['nickname'] = nick_ele.get_text(
            ).strip() if nick_ele else ''
            comment_ele = article_item.find(class_='ic-list-comments')
            article_info['comment_num'] = comment_ele.next_sibling.strip(
            ) if comment_ele else 0
            like_ele = article_item.find(class_='ic-list-like')
            article_info['like_num'] = like_ele.next_sibling.strip(
            ) if like_ele else 0
            money_ele = article_item.find(class_='ic-list-money')
            article_info['money_num'] = money_ele.next_sibling.strip(
            ) if money_ele else 0
            result.append(article_info)
        return result

    def searchDetail(self, link):
        detail = {
            'author': {},
            'article': ''
        }
        url = self.detailurl + link
        res = requests.get(url, headers=self.selfheaders)
        soup = BeautifulSoup(res.text, 'lxml')
        article = soup.find(class_='article')
        detail['title'] = article.find(class_='title').get_text().strip()
        author = article.find(class_='author')
        detail['author']['name'] = author.find(
            class_='name').get_text().strip()
        detail['author']['href'] = author.find(class_='avatar')['href']
        detail['author']['avatar'] = author.find(class_='avatar').img['src']
        detail['author']['publish_time'] = author.find(
            class_='publish-time').get_text().strip()
        detail['article'] = article.find(class_='show-content-free').prettify()
        return detail

    def searchMoreComments(self, article_id, params):
        root_url = 'https://www.jianshu.com/notes/'
        url = root_url + str(article_id) + '/comments'
        res = requests.get(url, params=params, headers=self.selfheaders)
        return res.json()

    def searchChildComments(self, comment_id='30210102', params_str='seen_comment_ids[]=30262461&seen_comment_ids[]=30262490&seen_comment_ids[]=30262567'):
        print(comment_id, params_str)
        root_url = 'https://www.jianshu.com/comments/'
        url = root_url + str(comment_id) + '/more_children?' + params_str
        res = requests.get(url, headers=self.selfheaders)
        return res.json()

if __name__ == "__main__":
    jianshu = JianShuInfo()
    # result = jianshu.searchDetail('/p/bfc7e7329cff')
    # result = jianshu.searchMoreComments('35345636', {
    #     'author_only': 0,
    #     'order_by': 'desc',
    #     'page': 1
    # })
    result = jianshu.searchChildComments()
    print(result)
    pass
