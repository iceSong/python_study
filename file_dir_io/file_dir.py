# -*- coding:utf-8 -*-

import os
import sys

print(os.name)  # 操作系统类型
# print(os.uname())  # 详细信息， 在windows平台不提供
print(os.environ)  # 环境变量
print(os.environ.get('JAVA_HOME'))  # 调取某一个环境变量的值

print(os.path.abspath('.'))  # 当前绝对路径
print(os.path.join('.', 'song'))  # 拼接路径，可用于跨平台（windows\, unix/), 切记不能够直接拼接
# .\song  ./song

print(os.path.split('D:\\workspace\\PythonWS\\python_study\\file_dir_io.py'))  # 拆分路径
# ('D:\\workspace\\PythonWS\\python_study', 'file_dir_io.py') 前面是路劲，后面是文件名
print(os.path.splitext('D:\\workspace\\PythonWS\\python_study\\file_dir_io.py'))  # 拓展名
# ('D:\\workspace\\PythonWS\\python_study\\file_dir_io', '.py')

l = [x for x in os.listdir('.') if os.path.isdir(x)]  # 当前目录中的目录
print(l)

# 列出后缀为.py的文件
l1 = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(l1)


# 作业
def dir_l(path):
    for d in os.listdir(path):
        print(d)


def find_file_name(path, key):
    print(path)

    for d in os.listdir(path):
        if os.path.isdir(d):
            find_file_name(os.path.abspath(d), key)
        if os.path.isfile(d):
            print(d)

# 有问题

if __name__ == '__main__':
    # dir_l(sys.argv[1])
    print('\n\n\n')
    find_file_name('D:\workspace\PythonWS\python_study', 'st')







