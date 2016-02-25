# -*- coding:utf8 -*-

import time, sys, queue
from multiprocessing.managers import BaseManager


# 创建类似的ManagerQueue
class QueueManager(BaseManager):
    pass

# 由于这个queue只是从网络上获取queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 链接到服务器，也就是运行manager的设备
server_addr = '127.0.0.1'
print('Connect to server %s' % server_addr)
# 端口和验证码保持与服务器上一致
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列获取任务，并把结果写入result队列
for i in task:
    try:
        n = task.get(timeout=1)
        print('run task %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, n*2)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty')
# 处理结果
print('worker exit')


