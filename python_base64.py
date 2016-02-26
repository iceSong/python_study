# -*- coding:utf8 -*-
# Base64是用64个字符来表示任意二进制数据的方式
# 将3个字节(24bit) 划分为4组（6bit), 得到四个数字索引，查表得到字符串
# 因此base64会把3字节的二进制数据转化为4字节的文本，长度增加33%

import base64

s = base64.b64encode(b'binary\x00string')  # 这样编码就是为了能够显示吗？内容不具备可读性啊
print(s)
d = base64.b64decode(s)
print(d)
print(base64.b64encode(b'iia'))  # b'aWlh' 三个字符编译为4个字符

# url safe base65
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))  # url safe能够将+和/转化为-和_

# base64适用于小段内容编码比如数字证书签名，因为=在url和cookie里会造成歧义，因此可以把末尾的=号去掉
# 解码时因为base64编码出的字串都是4的倍数，所以自动添加==


# 作业解码去掉了末尾等号的base64编码字串
def safe_base64_decode(s):
    tmp = 4 - len(s) % 4  # 3个字符，至多缺失2个
    if tmp == 4:
        return base64.b64decode(s)
    elif tmp == 1:
        return base64.b64decode(s + '=')
    elif tmp == 2:
        return base64.b64decode(s + '==')
    else:
        print('wrong! you may lost some required data')

print(safe_base64_decode('YweWJjZA'))

# Base64是一种任意二进制到文本字符串的编码
# 方法，常用于在URL、Cookie、网页中传输少量
# 二进制数据,减少传输量
