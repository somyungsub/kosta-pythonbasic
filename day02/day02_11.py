# -*- coding: utf-8 -*-
class A:
    def __init__(self):
        print ("Class A init")


class AC:
    def __init__(self):
        print ("Class AC init")

    def hello(self):
        print ("AC hello")


class B(A, AC):
    def __init__(self):
        super(B, self).__init__()
        # AC.__init__(self)

    def hello(self):
        print ("B hello")
        super(B, self).hello()

a = A()
ac = AC()
ac.hello()

b = B()

#c.hello()
