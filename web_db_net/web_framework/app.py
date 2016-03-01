# -*- coding:utf-8 -*-
# 使用Flask作为web框架编写web应用

from flask import Flask
from flask import require
from flask import render_temlate

app = Flask(__name__)


# @app.route('/', methods=['POST', 'GET'])
# def home():
#     return '<h1>Home</h1>'
#
#
# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#                <p><input name="username" /></p>
#                <p><input name="password" type="password" /></p>
#                <p><button type="submit">sign In</button></p>
#                </form>'''
#
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     # 需要从request获取对象读取表单内容
#     if request.form['username'] == 'admin' and request.form['password'] == 'password':
#         return '<h1>Hello, admin!</h1>'
#     return '<h1>Bad username or password</h1>'


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_temlate('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_temlate('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request获取对象读取表单内容
    username = request.form['username']
    passwd = request.form['password']
    if username and passwd:
        return render_temlate('signin-ok.html', username=username)
    return render_temlate('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run(debug=True)


# 其他可用框架
# DDjango：全能型Web框架；
# web.py：一个小巧的Web框架；
# Bottle：和Flask类似的Web框架；
# Tornado：Facebook的开源异步Web框架。

# 除了Jinja2，常见的模板还有：
# Mako：用<% ... %>和${xxx}的一个模板；
# Cheetah：也是用<% ... %>和${xxx}的一个模板；
# Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。



