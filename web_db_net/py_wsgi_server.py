# -*- coding:utf-8 -*-

# wsgi 服务器端
from wsgiref.simple_server import make_server

from web_db_net.py_wsgl import application

# 创建一个服务器IP为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)  # 设定端口，绑定处理函数
print('Serving HTTP on port 8000....')
# 开始监听http请求
httpd.serve_forever()