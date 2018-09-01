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

print(a['ab'])
print(a.get('ab'))
print(a.pop('ab'))

print(a)

# remove만 하는 경우
del a[(1, 2)]


a = {
    1: 'number'
    , 'ab': '문자열'
    , (1, 2): 'tuple'
}

# popitem
print(a.popitem())  # 튜플형식으로 반환
print(a)

a['python'] = 'python lov'
print(a)

# key영어가 첫문자는 영어로 시작하되, 영어 + 숫자 경우 가능   (1ab, 11, tuple.. 안됨)
a.update(ab=51231321)
print(a)


d2 = dict(abc=1235666)
print(d2)


# 더하기 불가능
# print(a + d2)   # 예외 발생
a.update(d2)    # update 메서드를 이용하여 합칠수 있음
print(a)        # a에 d2를 추가하여 a에 저장됨
print(d2)




# copy를 사용행함. slice는 인덱스 기반 a[:] 예외발생됨
d2 = a.copy()
print(d2)

# clear 모든 key 삭제
a.clear()
print(a)

# d2['ab'].append(11) # ??


