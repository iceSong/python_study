# -*- coding:utf8 -*-
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# collections是python内建的集合模块，拥有许多有用的集合

# tuple不可变集合
p = (1, 2)  # 比较难以看出表示坐标
# 使用namedtuple, 来创建一个类, 同时保持tuple的不变性
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
print(p1.x)
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素

print(p1, Point)
print(p1, tuple)

# 定义一个园
Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(2, 4, 7)
print(c.x, c.y, c.r)


# deque
# list 是线性存储数据，访问快插入删除慢，deque是能够高效插入删除的双向列表，使用与队列和栈
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')  # 想头部添加元素
print(q)
print(q.popleft())  # 从头部弹出元素
print(q)


# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希
# 望key不存在时，返回一个默认值，就可以用
dd = defaultdict(lambda: 'N/A')  # 添加函数，返回默认值，其他与dict完全一样
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])


# OrderedDict
# dict中的key是无序的，OrderedDict可以按照插入顺序排列
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)  # 每次输出的顺序都可能不一样
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)  # 输出有序，按照插入顺序输出
od['v'] = 4
od['t'] = 5
print(od)


# 使用orderedDict实现FIFO队列，当超过容量时删除最早添加的key
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self.__capacity = capacity

    def __setitem__(self, key, value):
        contains_key = 1 if key in self else 0
        if len(self) - contains_key >= self.__capacity:
            last = self.popitem(last=False)
            print('remove:%s' % last)
        if contains_key:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


# Counter
# Counter是一个简单的计数器
c = Counter()
for ch in 'programing':
    c[ch] += 1

print(c)