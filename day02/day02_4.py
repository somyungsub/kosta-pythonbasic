# -*- coding: utf-8 -*-

# while
a = True
i = 0

while a:
    if i == 10:
        break

    i += 1

    if i == 5:
        continue

    print (i)
else:
    print ("빠져나옴")


a = [1, 2, 3, 4, 5]
while a:
    j = a.pop()
    print (j)
else:
    print ("while else")    # 끝이라고 판단되는 경우 해당 됨

