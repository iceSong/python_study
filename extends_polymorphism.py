# -*- coding:utf-8 -*-
# 继承与多态, 鸭子类型


class Animal(object):
    def run(self):
        print('Animal is running')


class Cat(Animal):
    pass

cat = Cat()
cat.run()
