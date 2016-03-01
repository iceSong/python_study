# -*- coding:utf8 -*-
import struct

# struct的pack函数把任意数据类型变成bytes
print(struct.pack('>I', 10230099))

with open('python_struct.bmp', 'rb') as rf:
    bmp = rf.read(30)
    print(bmp)
    unpack_data = struct.unpack('<ccIIIIIIHH', bmp)
    print(unpack_data)

# BMP格式采用小端方式存储数据，文件头的结构按顺序如下： >
# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；     c
# 一个4字节整数：表示位图大小；                         I
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；                              H
# 一个2字节整数：颜色数。

