# -*- coding:utf-8 -*-
# asyncio python3.4内置的对异步io的支持库
# 将需要执行的协程放到asyncio的消息队列中

import asyncio

# @asyncio.coroutine
# def hello():
#     print('hello world')
#     # 异步调用asynio.seelp()模拟io耗时
#     r = yield from asyncio.sleep(1)  # yield from语法可以让我们方便地调用另一个generator
#     print('Hello again', r)
#
# # 获取EventLoop
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     writer.close()
#
# loop2 = asyncio.get_event_loop()
# tasks2 = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop2.run_until_complete(asyncio.wait(tasks2))
# loop2.close()


# async/await
# 为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
# 请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
# 1.把@asyncio.coroutine替换为async；
# 2.把yield from替换为await。


# 3.4写法
@asyncio.coroutine
def hello():
    print('Hello 1')
    r = yield from asyncio.sleep(1)
    print('hello again')


# 3.5写法
async def hello1():
    print('1-1')
    r = await asyncio.sleep(1)
    print('1-2')

loop = asyncio.get_event_loop()
loop.run_until_complete(hello1())  # 提供两个会报错？
loop.close()

