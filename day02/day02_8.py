# -*- coding: utf-8 -*-


a = 'a'


def a_func():
    print ("aaa")
    pass


def b_func():
    print ("bb")
    pass


adic = dict(a=a_func(), b=b_func())
value = adic['b']
