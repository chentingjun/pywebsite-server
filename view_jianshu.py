from flask import request
import json
from load_jianshu_list import JianShuInfo


def get_jianshu_article_list():
    res = {'msg': 'success', 'result': None}
    if request.method == 'GET':
        # offset = request.args.get('offset', 0)
        # limit = request.args.get('limit', 10)
        # res = op_sql.selectSql(
        #     'SELECT * FROM article_jianshu LIMIT %s, %s', (offset, limit))
        jianshu_info = JianShuInfo()
        pageno = request.args.get('pageno', 1)
        search = request.args.get('search', '')
        print('search', '----------', search)
        res['result'] = jianshu_info.searchList(pageno, search)
        return json.dumps(res)
    res = {'msg': 'post is error', 'result': None}
    return json.dumps(res)


def get_jianshu_detail(link=''):
    res = {'msg': 'success', 'result': None}
    if request.method == 'GET':
        if link != '':
            jianshu_info = JianShuInfo()
            res['result'] = jianshu_info.searchDetail(link)
        else:
            res['result'] = []
        return json.dumps(res)


def get_comments():
    res = {'msg': 'success', 'result': None}
    if request.method == 'GET':
        article_id = request.args.get('article_id', '')
        if article_id == '':
            res = {'msg': 'error', 'result': 'Invalid parameters'}
            return json.dumps(res)
        _author_only = request.args.get('author_only', 'false')
        author_only = 'true' if _author_only == 'true' else 'false'
        order_by = request.args.get('order_by', 'desc')
        page = request.args.get('page', 1)
        jianshu_info = JianShuInfo()
        res['result'] = jianshu_info.searchMoreComments(
            article_id, {'author_only': author_only, 'order_by': order_by, 'page': page})
    return json.dumps(res)


def get_children_comments():
    res = {'msg': 'success', 'result': None}
    if request.method == 'GET':
        comment_id = request.args.get('comment_id', '')
        if comment_id == '':
            res = {'msg': 'error', 'result': 'Invalid parameters'}
            return json.dumps(res)
        params_str = request.args.get('search', '')
        jianshu_info = JianShuInfo()
        res['result'] = jianshu_info.searchChildComments(
            comment_id, params_str)
    return json.dumps(res)

# 添加路由


def add_jianshu_routes(app):
    app.add_url_rule('/api/getjianshulist',
                     view_func=get_jianshu_article_list, methods=['GET'])
    app.add_url_rule('/api/getjianshudetail/<link>',
                     view_func=get_jianshu_detail, methods=['GET'])
    app.add_url_rule('/api/jianshucomments',
                     view_func=get_comments, methods=['GET'])
    app.add_url_rule('/api/childrencomments',
                     view_func=get_children_comments, methods=['GET'])
