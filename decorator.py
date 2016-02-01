# -*- coding: utf8 -8-
# 装饰器
# 函数也是一个对象，函数对象有一个__name__的属性，是函数的名称

from functools import wraps


def func1(x):
    return pow(x, 2)

func_obj1 = func1  #
print(func_obj1)
print(func_obj1.__name__)


# 定义能够打印日志的decorator
def log(func):
    def wrapper(*args, **kw):  # 为什么不直接卸载log函数中？ 再嵌套一层是什么意思？
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log2(desc):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (desc, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# 最终样式的装饰器
def log3(desc):
    def decorator(func):
        @wraps(func)  # 将函数名修正为传入函数的名字
        def wrapper(*args, **kw):
            print('%s %s', desc, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


@log3('带参数')  # 如此操作后，调用now函数时会自动执行log函数
def now():
    print('2016-2-1')

print('函数名称%s:' % now.__name__)


# 作业，打印begin call与end call
def log4(*text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            if text:
                print('%s begin call %s' % (text[0], func.__name__))
            else:
                print('begin call %s' % func.__name__)
            ax = func(*args, **kw)
            print('end call %s' % func.__name__)
            return ax
        return wrapper
    return decorator


@log4('加法')
def increment(x, y):
    return x + y


# 减法
@log4()
def decrement(x, y):
    return x - y

print(increment(3, 7))
print(decrement(9, 2))



