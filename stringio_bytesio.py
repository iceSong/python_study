# -*- coding:utf-8 -*-

# StringIO 在内存中读写str

from io import StringIO
from io import BytesIO

f = StringIO()
s = f.write('hello')
print(f.tell())  # 游标指向最后
print(f.readline())
f.seek(0)  # 游标指向最开始
print(f.readline())
print(s)  # 5 返回的是长度
print(f.getvalue())  # hello 返回值

f1 = StringIO('hello\nsong\ni\'m kangkang')
for line1 in f1.readlines():  # 像读取文件一样读取str
    print(line1.rstrip())

# StringIO只能够用于str，如果需要操作二进制数据则需要BytesIO
b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())
