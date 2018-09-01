# -*- coding: utf-8 -*-


# 다중 상속


class A:
    def hello(self):
        return 1


class B(A):
    def hello(self):
        return 2


class C(B, A):
    def hello(self): return 3


c = C()
c.hello()



