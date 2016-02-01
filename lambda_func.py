# -*- coding: utf8 -*-

# 计算x的平方
list1 = list(map(lambda x: x*x, [1, 234, 2, 5, 8]))  # map 会将function一次作用于每一个列表元素
print(list1)

# lambda表示匿名函数，冒号前面的x表示参数，
# 匿名函数只能够拥有一个表达式， 不需要写return,
# 返回值就是表达式的结果


# 匿名函数也是一个函数对象，可以赋值给变量
func1 = lambda x: x*x  # 并不推介这样写，编码习惯不好，此处仅是为了说明
print(func1(4))


# 结合上一节， 返回函数
def count(param):
    return lambda: param*param  # lambda函数的参数可以不写

f2 = count(4)
print(f2())

