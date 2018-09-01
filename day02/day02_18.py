# 데코레이터
# 또 다른 함수를 반환

from functools import wraps

def wrapf(func):
    k = True
    @wraps(func)
    def inner(*args, **kwargs):
        if k:
            return func(*args, **kwargs)
    return inner

def optf(arg1, arg2):
    def wrapf(func):
        k = True
        @wraps(func)
        def inner(*args, **kwargs):
            if k:
                return func(*args, **kwargs)
        return inner
    return wrapf



# @wrapf
# def f():
#     return 4
# print(f())




# @wrapf
@optf(True, False)
def f(k, j):
    """
        f 함수 입니다.
    """
    return 4
# print(f(1, j=4))
help(f)