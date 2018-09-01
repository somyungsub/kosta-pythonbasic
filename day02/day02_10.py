# -*- coding: utf-8 -*-


print (sum(range(1, 11)))

from functools import reduce

multi_accum = reduce(lambda x, y: x * y, range(1, 7))

print (multi_accum)


