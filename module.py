# -*- coding: utf-8 -*-
from PIL import Image

__author__ = 'song'


def func1():
    im = Image.open('test.jpg')
    print(im.format, im.size, im.mode)
    im.thumbnail((200, 100))
    im.save('thumb.png', 'PNG')


if __name__ == '__main__':
    func1()
