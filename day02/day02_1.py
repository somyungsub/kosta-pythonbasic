# -*- coding: utf-8 -*-
# if, for, while
b = 1

if b:
    pass    # 아무것도 하지 않고 if을 실행함 (일부로 만드는 경우)

# 조건문 if 형태
# 들여쓰기로 영역을 구분함(스코프 처리)
# 들여쓰기는 인덴트가 동일해야 함

if b:
    print (1)
    print (2)
    print (3)
elif b == 2:
    pass
    print (2222)
    print (2222)
else:
  print ("else 1")
  print ("else 2")
  print ("else 3")



# and, or , not
a = 3
b = 1
print (a and b)

c = a and b     # 1
print (c)

# or
c = a or b
print (c)

a = 0
b = 1
if a and b:
    pass
elif a or b:
    pass

# not
if not a:
    pass

# 우선순위 소괄호
# 튜플 -> 소괄호 생략 가능하나 명시해주는 것이 좋다
if (a and 1,2,3):
    pass

