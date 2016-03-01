# -*- coding:utf8 -*-

import itertools

# 用于操作迭代对象的函数

# natuals = itertools.count(1)  # 创建无限迭代器
# for n in natuals:
#     print(n)

# cs = itertools.cycle('abc')  # 无限循环给出的数据
# for c in cs:
#     print(c)

ns = itertools.repeat('A', 3)  # 可以限定重复次数
for n in ns:
    print(n)

# takewhile 截取无限循环中的数据
n = itertools.count(1)
ns1 = itertools.takewhile(lambda x: x < 10, n)
print(list(ns1))

# chain 把一组迭代对象串联起来
for c in itertools.chain('ABC', 'ZXC'):  # 链接
    print(c)

# groupby 相同的元素放在一起
for key, group in itertools.groupby('AABBCCCAAA'):
    print(key, list(group))  # A [A, A] B[B, B] C[C, C, C] A[A, A, A]

for key, group in itertools.groupby('AaaBBBbCCccD', lambda c: c.upper()):  # 只要前后两个值相等，就判定在一起
    print(key, list(group))  # 可以自定义挑选规则

