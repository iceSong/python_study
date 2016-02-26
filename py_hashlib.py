# -*- coding:utf8 -*-
import hashlib
# hashlib 提供常用的摘要算法，如md5, sha1等等

# md5
org_data = 'hello, mirror'
md5 = hashlib.md5()

md5.update('hwo to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5n = hashlib.md5()
md5n.update('hwo to use md5 in '.encode('utf-8'))
md5n.update('python hashlib?'.encode('utf-8'))  # 分两次写并不影响结果
print(md5n.hexdigest())


# sha1
sha1 = hashlib.sha1()
sha1.update('hwo to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())