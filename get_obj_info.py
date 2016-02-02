# -*- coding: utf-8 -*-
import types
# 获取对象信息
# type 函数
print(type(123))
print(type('hello'))
print(type(abs))
t = type(1211)
print(t == int)


def func1():
    pass

print(type(func1) == types.FunctionType)
print(isinstance(func1, types.FunctionType))

print(dir('as'))


class Student(object):  # len()实际是调用对象的__len__()方法
    def __init__(self):
        self.__name = 'song'
        self.__age = 12

    def __len__(self):
        return 20

print(len(Student()))
s = Student()
setattr(s, 'x', 2332)  # 绑定一个属性
print(hasattr(s, 'x'))  # 判断有没有属性
print(getattr(s, 'x'))  # 获取属性的值
print(getattr(s, 'y', 'default value'))  # 不存在则返回默认值



