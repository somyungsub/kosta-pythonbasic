# -*- coding: utf-8 -*-

# 함수
# 매개변수 , 리턴
# 블랙박스 (입 -> 출)
# a, b -> a + b


# def 함수명[영어, _, 한글, 숫자는 중간에](매개변수...)

import os


def _func():
    print ("aaa")


def _func2():
    print ("aaa222")
    return "222"


def _func3(arg1, arg2, arg3, arg4):
    print ("aaa3")
    return "3333"

# 기본값 인자 -> 매개변수 안넘길 경우 자동 세팅됨!
# 기본값 인자는 항상 필수 인자보다 뒤에 있어야한다 이유는 생략하는 부분때문에 판단에 모호성이 생기게 되므로..


def _func4(arg1=2, arg2=3, arg3=5):
    print (arg1, arg2, arg3)


def _func5(*args):
    print (args)
    print (args[0])

    for i in args:
        print (i)


def _func6(*args):
    print ("C:\\{}".format("\\".join(args)))
    print ("C:{}".format(os.sep.join(args)))


# 인자 순서 필수인자>기본인자>가변인자
def _func7(arg1, arg2=2, *args):
    print (arg1, arg2, args)




print (_func())
print (_func2())
print (_func3(1, 2, 3, 4))
print (_func4(1, 2))
print (_func5(1, 2, 3, 4, 5, 6, '1234', "777", '4444'))


# c:/
# c:/Window/System32/Drivers/etc/hosts

path = ("Window", "System32", "Drivers")
print ("\\".join(path))
_func6("Window", "System32", "Drivers", "etc", "hosts")
_func7(1)
_func7(1, 2)


# def 한글명():
#     print ("bbbbb")
#     print ("bbbbb")
#     print ("bbbbb")
#     print ("bbbbb")
#     print ("bbbbb")
#
# 한글명()
