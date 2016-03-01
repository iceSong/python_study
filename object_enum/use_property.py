# -*- coding:utf-8 -*-

# 使用@property


class Student(object):
    def __init__(self):
        self._score = 0

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score mast be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

s1 = Student()
s1.set_score(98)
print(s1.get_score())


# 使用property
class Person(object):
    @property
    def score(self):
        return self._score  # 当变量名与方法名向同时，使用@score.setter会循环递归

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value  # 注意出现循环递归

p1 = Person()
p1.score = 78  # 将方法转变成属性那样调用
print(p1.score)


# 作业
class Screen(object):
    def __init__(self):
        self._width = 0
        self._height = 0
        self._resolution = 'no way'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._resolution

s = Screen()
s.width = 100
s.height = 80
print(s.resolution)


