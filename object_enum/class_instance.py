# -*- coding: utf-8 -*-


class Student(object):
    pass

stu1 = Student()
stu2 = Student()
print(stu1, stu2)
stu1.name = 'hahaha'  # 居然可以在外面随意绑定属性？？？？？？
print(stu1.name)


class Person(object):
    def __init__(self, name, age, phone):  # 构造方法，self是类中的函数都要的，表示自己，使用的时候并不需要传递self
        self.name = name  # 绑定属性，hahhaha哪里应该是一样的
        self.__age = age  # __age 前面的 __ 表示这是一个私有变量，外部不能直接访问, 被解释成了_Person__age, 所以可以通过instance._Person__age访问
        self._phone = phone  # _phone 前面的 _ 表示这是一个外部可以访问的私有变量，但是最好不要直接访问

    def print_info(self):
        print('name: %s\n age: %d' % (self.name, self.__age))

my = Person('song', 23, '18811449845')  # 初始化，并不需要传递self参数，Python解释器会自动完成
my.print_info()
print(my.name)  # OK
print(my._phone)  # 不建议
# print(my.__age)  # 报错
print(my._Person__age)  # 强烈不建议这么干，这取决于python解释器，万一不解释成这样就没法用了


# ---------------------------------------------------------
# 实例属性与类属性
# ---------------------------------------------------------
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.age = 10
print(s.name, s.age)  # name, age 都是实例属性，归实例所有


class Person(object):
    name = 'Mical'  #类属性

p = Person()
print('类属性 %s' % p.name)
p.name = 12  # 绑定实例属性
print(p.name)  # 因为类属性的优先级不如实例属性高，所以先检测实例属性，类属性被覆盖
print(Person.name)  # 但是此时类属性任然在内存中存在，用类名可以访问
del p.name  # 删除实例的name属性后，类属性又可见了
del Person.name
print(p.name, '---')
