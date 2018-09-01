# -*- coding: utf-8 -*-

# 중첩함수
def f():
    def f2():
        return 4

    a = f2()
    return a + 1


print (f())

al = [1, 2, 3, 4, 5]
alr = []
for entry in al:
    if entry > 2:
        alr.append(entry)

print (alr)

# 람다
for entry in al:
    if (lambda x: x > 2)(entry):
        alr.append(entry)

print (alr)

# 람다 함수 -
aa = (lambda x, y, z, *args, **kwargs: kwargs)(1, 2, 3, color=4)
print (aa)

alr2 = filter(lambda x: x > 2, al)
print (alr2)

map2 = map(lambda x: x * 2, alr2)
print (map2)



