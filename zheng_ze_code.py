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
print('正则切分:', re.split(r'\s+', str1))



