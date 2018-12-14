from flask import Flask
import os
from views.index import CreateViews

app = Flask(__name__)
CreateViews(app)
app.config['SECRET_KEY'] = os.urandom(24)  # 随机产生24位的字符串作为SECRET_KEY
if __name__ == "__main__":
    app.run(debug=True)
    pass
