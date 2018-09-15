from flask import Flask

app = Flask(__name__)


# 使用@app.route('/')装饰器
# 可以让用户在访问网站根页面 http://<site_name>/ 时自动调用被装饰的函数
@app.route('/')
def hello_world():
    return 'Hello World!<br/>第一个Python flask app asd'


if __name__ == '__main__':
    app.config.from_pyfile()
    app.run()
