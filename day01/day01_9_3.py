st1 = {1, 2, 3, 4}
st2 = {3, 4, 5, 6}
st3 = {1, 2}

print(st3.issubset(st1))  # st3기준 st1이 아래 집합인가?
print(st1.issuperset(st3))  # st1기준 st3이 부모 집합인가?

print(st3)
print(st3.pop())
print(st3)

# 반복가능한 것 만 가능 (문자열, 리스트, 튜플, 사전...)
# 데이터 타입 (숫자-정,실,복, 문자열, 튜플) / 리스트 또 다른 집합 -> 다른요소로 추가 불가능 따라서
print(st3.update('ab'))
print(st3.update(['a2', 'b2']))
print(st3)

# 삭제
st4 = st3.copy()
st3.clear()
print(st3)

# 복사 [:]은 안됨 index 기반아님
print(st4)

# bool - 조지 부울이 만들어서 bool
# 모든 파이썬의 상태 값  True / False

a = True
b = False

print(a & a)
print(a & b)
print(b & a)
print(b & b)

print(a | a)
print(a | b)
print(b | a)
print(b | b)

print("--------------------")
c = bool()
d = bool(0)

print(c)
print(d)

print("--------------------")
bb = None  # null과 같은 의미

# in 키워드 - 문자열이 있는지 / 사전 - key가 있는지 / 집합 -
# in 키워드 안됨 - 숫자 실수 복소수는
str = "Hello Python"
print(str.find("Python"))
print("Python" in str)  # 있으면 True 없으면 False
print("a" not in str)  # 없으면 True 없으면 False

print(str * 3)
print(str + str)
print(3 * str)
print(len(str))

print(min(10, 20))
print(max(10, 20))

print(min("eaaaabasadqA"))  # 아스키 값 최소
print(max("eaaaabasadqA"))  # 아스키 값 최대

print(sum(range(1, 11)))
print(sum(range(1, 101)))
print(sum(range(1, 1001)))

print(sum([1, 2, 3, 4, 5, 6]))

i1 = 10
b1 = bin(i1)
o1 = oct(i1)
h1 = hex(i1)

print(b1)
print(o1)
print(h1)

print(int(b1, 2))
print(int(o1, 8))
print(int(h1, 16))

# 대입연산자
i1 += 1
i1 -= 1
i1 /= 1
i1 *= 1
i1 //= 1
i1 %= 1

l1 = [1, 2, []]
l2 = l1.copy()
print(l1)
print(l2)


l1[-1].append(4)
print(l1)
print(l2)
