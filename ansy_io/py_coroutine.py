# -*- coding:utf-8 -*-
# 协程，又称微线程，纤程。英文名Coroutine
# 最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，
# 而是由程序自身控制，因此，没有线程切换的开销，和多线程比，
# 线程数量越多，协程的性能优势就越明显。
# 二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存
# 在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状
# 态就好了，所以执行效率比多线程高很多。

# Python对协程的支持通过generator实现


# 使用协程实现生产者消费者模型
def consumer():
    r = '----'
    while True:
        n = yield r  # 返回r, n是调用者传递过来的参数 协程的关键
        if not n:
            return
        print("[CUSTOMER] consuming %s" % n)
        r = '200 OK ' + str(n)  # 用传递过来的参数生成下一个返回值


def produce(c):
    print(c.send(None))
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # 切换到consumer执行，传递参数给生成器，并接受返回值
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()  # 关闭consumer

c = consumer()
produce(c)

# “子程序就是协程的一种特例。”
