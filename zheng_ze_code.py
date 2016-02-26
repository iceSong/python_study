# -*- coding:utf8 -*-
# python中\需要用\转义 所以 \\， 因此使用python的r前缀，这样字符串不用转义 \
import re
zheng_ze = r'^\d{3}\-\d{3,8}$'  # 对正则字串使用r前缀
a = re.match(zheng_ze, '010-233')  # 匹配
print(a)
b = re.match(zheng_ze, '2s-12123')  # 不匹配
print(b)
c = 'sds\'f'
print(c)

# 利用正则表达式切分字符串
str1 = 'a b    c'
print('按照空格正常切分:', str1.split(' '))  # 按照空格正常切分
print('正则切分:', re.split(r'\s+', str1))  # 按照正则表达式切分
print('正则:', re.split(r'[\s,;]+', 'a,b;; c   d'))

# 分组
m = re.match(r'^(\d{3})\-(\d{3,8})$', '010-123456')
print(m.group(0), m.group(1), m.group(2))  # group(0)表示原始字符

# 正则表达式采取贪婪匹配法
print(re.match(r'^(\d+)(0*)$', '102300').groups())  # ('102300', '') 前面匹配完了，后面没有匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 作业
pattern1 = r'^.+@[0-9a-z]+.com$'
print(re.match(pattern1, 'aaa@gmail.com'))
print(re.match(pattern1, 'bill.gates@126.com'))

pattern2 = r'^(<[-\w\s_\.]+>)?\s*([\w_\.-]+)@([\w_\.-]+)$'
print(re.match(pattern2, '<Tom-Paris> tom@voyager.org'))