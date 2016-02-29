# -*- coding:utf8 -*-
from urllib import request, parse

# urllib提供了一系列操作url的功能

# get
# request模块抓取url内容
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()  # 获取数据
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():  # 获取头
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))  # 解码


# 伪装成浏览器发送get请求
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU IPhone OS 8_0 like Mac'
                             ' OS X) AppleWebkit/536.26 (KHTML, like Gecko) Vers'
                             'ion/8.0 Mobile/10A5376e Safari/8635.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


# Post
# 发送Post请求只需要将参数data以bytes形式传入

print('Login to weibo.cn....')
email = input('Email:')
passwd = input('Password:')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%Fm'
                  '.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like '
                             'Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&re'
                          's=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:  # 把数据写成bytes
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


