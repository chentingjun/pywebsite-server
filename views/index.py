
from views.view_jianshu import add_jianshu_routes
from views.view_common import add_common_routes


class CreateViews():
    def __init__(self, app):
        add_jianshu_routes(app)
        add_common_routes(app)
