# -*- coding:utf-8 -*-

'''
多重继承
'''


class A(object):
    def run(self):
        print('A running')


class B(object):
    def run(self):
        print('B running')


class C(A, B):
    pass


class D(B, A):
    pass


C().run()
D().run()
