# -*- coding: utf-8 -*-

# f = open('file_io.py', 'r')  # 获得文件对象
# s = f.read()  # 将文件内容全部读入内存, 用str对象表示
# print(s)

# f.close()  # 关闭文件，一定

try:
    f = open('file_io.py', 'r')
    # print(f.read())
finally:
    if f:
        f.close()

# 指定目标文件的编码：encoding='utf-8' ， errors='ignore'表示遇到错误时忽略
with open('file_io.py', 'r', encoding='utf-8') as rf:
    print(rf.read())  # read(10) 指定读取的字节，大文件使用

# r读取文本文件， rb读取二进制文件， r+读取/创建， w写文本文件，w+写/创建， wb ..




