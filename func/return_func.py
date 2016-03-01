# -*-coding:utf-8 -*-
# 函数作为返回值， 高阶函数把函数作为返回值


# 可变参数求和
def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax


# 不要求立即求和，而是到需要的时候再计算
def lazy_sum(*args):
    def _sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return _sum  # 返回求和函数

f = lazy_sum(1, 23, 4, 5, 2, 4)
print(f)
print(f())


# -----------闭包----------------
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i  # 重要，闭包中不要引用任何循环变量，可能到使用时，值已经发生了变化
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())


# 如果一定要使用循环变量，则可以再增加一个函数
def count():
    def fu1(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(fu1(i))  # f1函数被执行，循环变量已经被使用, lazy加载g函数(g函数=闭包中已经保存了运算所需的数据
    return fs

for n in count():
    print(n())

