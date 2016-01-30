# -*- coding: utf-8 -*-

from functools import reduce

def f(s):  
    return int(s)


def g(x, y):
    y /= pow(10, len(str(y)))
    return x + y
    
  
l = reduce(g, map(f, '1234.45'.split('.')))
print(l)


