from flask import Flask, request
from operate_sql import OpSql
from load_jianshu_list import JianShuInfo
import json

app = Flask(__name__)
op_sql = OpSql()


@app.route('/news', methods=['GET'])
def show_users():
    if request.method == 'GET':
        new_id = request.args.get('new_id', -1)
        print(new_id)
        if new_id == -1:
            return 'not found'
        res = op_sql.selectSql(
            'SELECT * FROM article_spider WHERE id=%s', (new_id))
        return json.dumps(res)
    return 'POST'


@app.route('/api/getjianshulist', methods=['GET'])
def get_jianshu_article_list():
    res = {'msg': 'success', 'result': []}
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
    return res


@app.route('/api/getjianshudetail/<link>', methods=['GET'])
def get_jianshu_detail(link=''):
    res = {'msg': 'success', 'result': []}
    if request.method == 'GET':
        if link != '':
            jianshu_info = JianShuInfo()
            res['result'] = jianshu_info.searchDetail(link)
        else:
            res['result'] = []
        return json.dumps(res)


# https://www.jianshu.com/notes/33099094/comments?author_only=false&&order_by=desc&page=1
@app.route('/api/jianshucomments', methods=['GET'])
def get_comments():
    res = {'msg': 'success', 'result': []}
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

@app.route('/api/childrencomments', methods=['GET'])
def get_children_comments():
    res = {'msg': 'success', 'result': []}
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

if __name__ == "__main__":
    app.run(debug=True)
    pass
