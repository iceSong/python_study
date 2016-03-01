# -*- coding:utf-8 -*-


# web_db_net server gateway interface
def application(environ, start_response):
    start_response('200 OK', [('Context-Type', 'text/html')])  # 该函数只能够被调用一次
    print(environ)
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web_db_net')
    return [body.encode('utf-8')]



