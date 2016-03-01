# -*- coding: utf8 -*-
# 偏函数
from functools import partial

# int()将字符串转化为整数， 有一个base命名关键字参数用于指定进制
print(int('123', base=8))


def int2(x, base=2):
    return int(x, base)

int8 = partial(int, base=8)  # partial 函数就是固定函数的某些参数的值

print(int2('10001110'))
print(int8('1234'))
