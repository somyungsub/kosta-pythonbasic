
# 객체끼리 연산

class A:
    def __add__(self, other):
        return 1 + other.k

    def __radd__(self, other):  # r 붙이면 기준을 바꿈
        return 1 + other.k

    def __sub__(self, other):
        return 10 - other.k

    def __mul__(self, other):
        return 2 * other.k

    def __truediv__(self, other):
        return 20 / other.k


class B:
    k = 4


a = A()
b = B()


print(a + b)
print(b + a)
print(a - b)
print(a * b)
print(a / b)
