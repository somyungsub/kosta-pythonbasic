

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





class MixIn:
    def print(self):
        print(self.i, self.k)

        print(self.i, self.k)


class C(MixIn):
    def __init__(self):
        self.i = 3
        self.k = 4


class D(MixIn):
    def __init__(self):
        self.i = 6
        self.k = 7

