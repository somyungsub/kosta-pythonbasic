# -*- coding: utf-8 -*-

# 값 = 조건 ? 참 : 거짓

cond = 1;
value = True if cond else "10"

print (value)

for i in [1, 3, 5, 7, 9, 11]:
    print (i)


# range 클래스 활용
print (range(10))

for i in range(10):
    print (i)

for i in range(1, 11):
    print (i)

for i in range(1, 11, 2):
    print (i)


print (sum(range(1, 11)))


print (range(1, 11))
print (list(range(1, 11)))
print (tuple(range(1, 11)))
print (set(range(1, 11)))


l1 = []
for item in range(1, 6):
    l1.append(item * 2)

print (l1)

l2 = [item * 2 for item in range(1, 6) if item != 2]
print (l2)
