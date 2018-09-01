# -*- coding: utf-8 -*-


def f(a, b, c, d, f=None, g=None):
    print (a, b, c, d, f, g)
    pass


# 키워드 인자 전달방식
f(a=1, b=2, c=3, d=4)
f(d=10, b=22, c=31, a=42)
f(d=10, b=22, c=31, a=42, f=10, g=25)


# 가변인자 - 사전
def f2(**kwargs):
    print (kwargs)
    print (kwargs['b'])


f2(d=10, b=22, c=31, a=42, f=10, g=25)


def f3(a, b, c, d):
    print (a, b, c, d)


k = [1, 2, 3, 4]
f3(*k)

k = dict(a=1, b=2, c=3, d=5)
f3(**k)

