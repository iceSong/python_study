# -*- coding:utf-8 -*-

# 多进程， unix/linux系统中fork()函数调用一次返回两次，系统复制一次父进程，得到子进程
# 子进程返回0，父进程返回子进程ID
import os
import time
import random
from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue
import subprocess


print(os.getpid())  # 获取当前进程id

# pid = os.fork()  # only works on unix/linux
# if pid == 0:
#     print('child process %s, parent process %s' % (os.getpid(), os.getppid()))
# else:
#     print('I\'m %s, child %s' % (os.getpid(), pid))


# windows 下python多进程
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


# 进程池
def long_time_task(name):
    print('Run task %s (%s)..' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, end - start))


# 写数据进程
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue' % value)


if __name__ == '__main__':
    # 创建进程
    print('Parent process %s.' % (os.getpid()))
    p = Process(target=run_proc, args=('test',))  # 创建子进程，需要函数，参数是元组
    print('Child process will start.')
    p.start()  # 启动进程
    p.join()  # 等待子进程结束才继续运行
    print('Child process end.')

    # 进程池
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done.')
    p.close()  # close 之后不能够再添加新的进程
    p.join()  # 在join之前必须调用close
    print('All done')

    # 子进程
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)

    # 进程间通信
    q = Queue()

    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()  # 启动写进程
    pr.start()  # 启动读进程

    pw.join()
    pr.terminate()  # 强制终止pr进程


