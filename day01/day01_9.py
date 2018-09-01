# 사전
# key, value로 구성 Java(Map과 비슷한 개념), PHP(연관배열)
# 수정 삭제 가능

a = {}
b = dict()  # 빈사전으로 초기화

print(a)
print(b)

a = {
    1: 'number'
    , 'ab': '문자열'
    , (1, 2): 'tuple'
}

print(a)

print(a.get(1))
print(a.get('ab'))
print(a.get((1, 2)))

print(a[1])
print(a['ab'])
print(a[(1, 2)])

# 삽입하기
a['22'] = 'aaa'
a['python'] = 'Hello python'
a[1] = 'poi'    # key가 있는 경우 오버라이딩 -> 이유는 []안의 값은 인덱스가 아닌 key값이 되기 때문
print(a)

# print(a["bbbbbbb"]) # key가 없는 경우 KeyError 예외발생
print(a.get(1))
print(a.get(11111)) # 키가 없는 경우 -> None
print(a.get(11111, "없는 경우 반환되는 값"))
print(a.get(11111, -1))

p = None
print(p)

# keys
print("----------------------------------------")
print(a.keys())
print(type(a.keys()))

print(list(a.keys()))
print(list(a.keys())[0])
print(list(a.keys())[1])
print(list(a.keys())[2])
print(list(a.keys())[3])

print(tuple(a.keys()))
print(tuple(a.keys())[0])
print(tuple(a.keys())[1])
print(tuple(a.keys())[2])
print(tuple(a.keys())[3])



# values
print("----------------------------------------")
print(a.values())
print(type(a.values()))

print(list(a.values()))
print(list(a.values())[0])
print(list(a.values())[1])
print(list(a.values())[2])
print(list(a.values())[3])

print(tuple(a.values()))
print(tuple(a.values())[0])
print(tuple(a.values())[1])
print(tuple(a.values())[2])
print(tuple(a.values())[3])

# key, value 동시에    -> 반한되는 item은 (key,value)의 튜플형식
print("----------------------------------------")
print(a.items())
print(type(a.items()))

print(list(a.items()))
print(list(a.items())[0])
print(list(a.items())[1])
print(list(a.items())[2])
print(list(a.items())[3])

print(tuple(a.items()))
print(tuple(a.items())[0])
print(tuple(a.items())[1])
print(tuple(a.items())[2])
print(tuple(a.items())[3])


# 튜플 -> 사전으로
print("----------------------------------------")
d4 = ((1, 'poi'), ('ab', '문자열'), ((1, 2), 'tuple'), ('22', 'aaa'), ('python', 'Hello python'))
d5 = dict(d4)
print(d5)


# list <-> 튜플 -> 사전 / 사전 -> 튜플 (key만 튜플로됨)

d6 = tuple(d5)
print(d6)