# -*- coding:utf-8 -*-
# 使用Flask作为web框架编写web应用

from flask import Flask
from flask import require

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
               <p><input name="username" /></p>
               <p><input name="password" type="password" /></p>
               <p><button type="submit">sign In</button></p>
               </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request获取对象读取表单内容
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h1>Hello, admin!</h1>'
    return '<h1>Bad username or password</h1>'


if __name__ == '__main__':
    app.run()
