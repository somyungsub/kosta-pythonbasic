# -*- coding: utf-8 -*-

# 반복문 for, while

# 반복변수
for a in [1, 2, 3, 4]:
    print (a)

# 튜플
for a in (1, 2, 3, 4):
    print (a)

# 사전을 이용한 방법
c = dict(a=1, b=2, c=3)
for a in c:
    print (c.get(a))

# 사전 -> item : 튜플형태로 반환
for a in dict(a=1, b=2, c=3).items():
    print(a)

# 언패킹 -> a의 튜플을 분리해서 bcd에 들어감
# a = (1, 2, 3)
# b, c, d = a

for key, value in dict(a=1, b=2, c=3).items():
    print (key, value)
else:
    print ("else 절 실행") # 반복조건이 거짓일 때 실행 됨, but 거의 사용 하지 않음



