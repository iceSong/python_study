# -*- coding:utf-8 -*-
import socket
import threading

# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com.cn', 80))  # 参数是一个tuple 地址，端口
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接受数据
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('py_socket_sina.html', 'wb') as f:
    f.write(html)


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break;
        sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
        sock.close()
        print('Connection from %s:%s closed' % addr)

# server端
s = s.socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


