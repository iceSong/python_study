# -*- coding:utf-8 -*-
# 序列化， pickling

import pickle
import json

d = dict(name='bob', age=20, score=100)
a = pickle.dumps(d)  # 把任意对象序列化成一个bytes
print(a)

with open('dump.txt', 'wb+') as wf:
    pickle.dump(d, wf)

with open('dump.txt', 'rb') as rf:
    print(pickle.load(rf))  # 反序列化
# pickle进行序列化的内容不能够兼容其他语言，不同python版本间也可能不兼容，不能够用来保存重要的内容

# json
d = dict(name='bib', age=20, score=98)
j = json.dumps(d)  # 转化为json串
print(j)

dic = json.loads(j)  # 将json串转化为dict
print(dic)


# json序列化对象
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 89)

print(json.dumps(s, default=lambda x: {'name': x.name, 'age': x.age, 'score': x.score}))  # 指定转化方法
print(json.dumps(s, default=lambda obj: obj.__dict__))  # 把任意的对象转化成dict，通常的class都有一个__dict__属性
ss = json.dumps(s, default=lambda x: {'name': x.name, 'age': x.age, 'score': x.score})
# json转化为对象
d = json.loads(ss, object_hook=lambda dd: Student(dd['name'], dd['age'], dd['score']))  # 指定转化方法
print(d, d.name)




