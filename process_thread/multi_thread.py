# -*- coding:utf-8 -*-
# python 多线程
# python的线程是Posix Thread, Python提供了两个模块，_thread和threading, 后者对前者进行了封装

import time
import threading
import multiprocessing


# 新线程的执行代码
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 2:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')  # 创建新的线程
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)

# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于
# 每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何
# 一个变量都可以被任何一个线程修改

balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance -= n
    balance += n


def run_thread(n):
    for i in range(1000000):
        lock.acquire()  # 获取锁
        try:
            change_it(i)
        finally:
            lock.release()  # 释放锁

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(7,))

t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


def death():
    x = 0
    while True:
        x ^= 1

for i in range(multiprocessing.cpu_count()):
    threading.Thread(target=death).start()


# python解释其中的GIL(Global Interpreter Lock)会锁住所有python线程，每
# 个python线程交替执行100条字节码， 所以同一进程中永远只用一个python线程处于执行中
# 也导致python不能够有效利用多核cpu, 在多核上还是应该使用multiprocess

# ThreadLocal, 用于绑定线程中的局部变量，减少传递参数
local_school = threading.local()


def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start(), t2.start()
t1.join(), t2.join()
