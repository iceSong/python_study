# -*- coding: utf-8 -*-
# 面向对象高级编程
from types import MethodType


class Student(object):
    pass

s = Student()
s1 = Student()
s.name = 'Bob'  # 动态绑定属性
# print(s.name, s1.name)  # 对实例进行动态绑定只能绑定到当前实例


def set_age(self, age):
    self.age = age

s.set_age = MethodType(set_age, s)  # 给实例绑定方法，只对当前实例有作用
s.set_age(25)
print(s.age)


def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, Student)  # 给类绑定方法
s2 = Student()
s2.set_score(100)  # 绑定到类的属性和方法都是全局的，一个修改，处处变动
print(s2.score)  # 100
s3 = Student()
print(s3.score)  # 也是100，因为s2和s3共用class的score属性


# 限定实例中可以添加的属性
class Person(object):
    __slots__ = ('name', 'age')  # tuple中包含可以被使用的属性

p = Person()
p.name = 'KK'
setattr(p, 'age', 12)  # 添加属性
# p.weight = '200t'  # AttributeError: 'Person' object_enum has no attribute 'weight'

p1 = Person()
# print(p1.name)  # 没有为p1添加属性name


# 结论slots中定义的的属性只能够在当前类的实例中起作用，其子孙类并没有这些属性
class Chinese(Person):
    pass

c1 = Chinese()
c1.name = '2323'
c1.weight = '12t'
print(c1.weight)


class Animal(object):
    def __init__(self):
        self.name = '233-animal'


class Dog(Animal):
    def __init__(self):
        self.name = '233-dog'

d1 = Dog()
print(d1.name)


























