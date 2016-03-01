# -*- coding:utf-8 -*-

# ---------------对list进行排序-------------------------
list1 = [34, 1, 32, 75, 3]
print('origin:', list1)
print(sorted(list1))

# ------------sorted接受一个函数 key=function, 可以用来对待排序数据进行处理---------------------
list2 = [12, -34, -234, 3434, 234]
print('origin:', list2)
print(sorted(list2, key=abs))

# ---------对字符进行排序，字符默认按照ASCII比较，因此a>Z--------------------
list3 = ['as', 'dsd', 'ZX', 'Acv', 'cfb', 'Df']
print('origin:', list3)
print(sorted(list3))
print(sorted(list3, key=str.lower))
print(sorted(list3, key=str.lower, reverse=True))

# --------------练习-----------------------
L = [('Bob', 75), ('Adam', 92), ('Lisa', 88), ('as', 23)]


# 对列表中的tuple进行排序
def tuple_sorted_by_name(parameter):
    return parameter[0].lower()


print(sorted(L, key=tuple_sorted_by_name))
print(sorted(L, key=tuple_sorted_by_name, reverse=True))
