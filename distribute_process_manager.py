# -*- coding:utf8 -*-
# 分布式进程，managers模块支持将多进程分布到多台机器上

import random
import queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接受任务的队列
result_queue = queue.Queue()


# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass


def server():
    # 把两个Queue都注册到网络，callable参数关联了Queue对象
    QueueManager.register('get_task_queue', callable=task_queue)
    QueueManager.register('get_result_queue', callable=result_queue)

    # 绑定端口5000，设置验证码'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue
    manager.start()
    # 获得通过网络访问的queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务
    for i in range(10):
        n = random.randint(0, 1000)
        print('Put task %d...' % n)
        task.put(n)

    # 从result队列上读取结果
    print('Try get results..')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result %s' % r)

    # 关闭
    manager.shutdown()
    print('manager exit')

if __name__ == '__main__':
    server()