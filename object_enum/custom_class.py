# -*- coding:utf-8 -*-

'''定制类'''

__author__ = 'song'


class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Michael'))  # <__main__.Student object_enum at 0x007DD2B0>


# 定制类的输出，类似java中的头String()方法
class Student1(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):  # __str__()函数可以被print函数调用， __len__()可以被len()调用
        return 'Student1 object_enum (name: %s)' % self.name

    __repr__ = __str__  # __str__（）返回数据给用户， __repr__()返回数据给开发者，如此在控制台直接输入实例，得到的也一样了

print(Student1('Maria'))  # Student1 object_enum (name: Maria)


# 使自己的类可以用于for in循环， 实现__iter__()方法，返回一个迭代对象, 调用该对象的__next__()
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器

    def __iter__(self):
        return self  # __iter__中要求返回一个含有__next__方法的对象
        # return S()
        # return S1()  # TypeError: iter() returned non-iterator of type 'S1' 没有__next__则不是迭代器

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:  # 退出循环条件
            raise StopIteration()
        return self.a


class S(object):
    def __next__(self):
        return 'ddd'


class S1(object):
    pass

for n in Fib():
    print(n)

# for n in S():  # TypeError: 'S' object_enum is not iterable  有__iter__是可迭代对象
#    print(n)


# 能够按照下标取出元素 __gtitem__ 方法
class Fib1(Fib):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f1 = Fib1()
print(f1[2])  # 用下标取出元素
# print(f1[0:2])  # TypeError: 'slice' object_enum cannot be interpreted as an integer
# slice来确定是不是切片 isinstance(n, slice)  n.start  n.stop等


# __getattr__方法动态的返回一个属性
class Student(object):
    def __getattr__(self, item):  # 如果对象还没有绑定score对象，在调用score属性时就会自动调用getattr方法
        if item == 'score':  # 对于没有列出的则返回None, 可以手动抛出异常
            return lambda: 5
        raise AttributeError('\'Student\' object_enum has no attribute \'%s\'' % item)  # 这样当调用除了score以外的尚未定义的属性就会报错
#  怎么用。。。？


# 在实例本身上调用 __call__
class Student3(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s' % self.name)

s = Student3('song')
s()  # 直接调用实例


# 判断一个变量是对象还是函数。能够被调用的对象是Callable对象
print('判断对象是否可以调用 %s' % callable(Student3('df')))




