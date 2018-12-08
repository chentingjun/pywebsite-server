from flask import Flask, request
from view_jianshu import add_jianshu_routes
from view_common import add_common_routes
from operate_sql import OpSql
import json

app = Flask(__name__)
op_sql = OpSql()

# 添加其他路由
add_jianshu_routes(app)
add_common_routes(app)


@app.route('/test', methods=['GET'])
def show_users():
    return 'hello world'


if __name__ == "__main__":
    app.run(debug=True)
    pass
