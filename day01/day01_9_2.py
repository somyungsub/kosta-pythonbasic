# 집합    빠른 연산을 하기 위한 자료구조
# ex) DB 작업 -> 종이자료 500장 - 목록(엑셀) 500장 스캔 -> 실수
# 연산자를 적극 활용    Java의 set과 유사
# 중복데이터는 원데이터 처리(중복허용x), 순서 x

se1 = set()
se1.add(1)
se1.add("abcd")
print(se1)

se2 = {1, 2, 3, 4, 5, 6}  #
print(se2)
t1 = [6, 5, 1, 2, 6]
se3 = set(t1)  # 중복데이터는 1데이터 처리
print(se3)


# 집합연산
st1 = {1, 2, 3, 4}
st2 = {3, 4, 5, 6}
st3 = {1, 2, 3, 7}

# 교집합
print(st1.intersection(st2))    # st1 st2 교집합
print(st1.intersection(st3))    # st1 st3 교집합
print(st1.intersection(st2).intersection(st3))  # # st1 st2 st3 교집합

print(st1 & (st2))    # st1 st2 교집합
print(st1 & (st3))    # st1 st3 교집합
print(st1 & (st2) & (st3))  # # st1 st2 st3 교집합



# 합집합
print(st1.union(st2))    # st1 st2 합집합
print(st1.union(st3))    # st1 st3 합집합
print(st1.union(st2).union(st3))  # # st1 st2 st3 합집합

print(st1 | (st2))    # st1 st2 합집합
print(st1 | (st3))    # st1 st3 합집합
print(st1 | (st2) |(st3))  # # st1 st2 st3 합집합


# 차집합
print(st1.difference(st2))    # st1 st2 차집합 (st1 - st2)
print(st1.difference(st3))    # st1 st3 차집합 (st1 - st3)
print(st1.difference(st2).difference(st3))  # # st1 st2 st3 차집합 ((st1 - st2) - st3)

print(st1.difference(st2))    # st1 st2 차집합 (st1 - st2)
print(st1.difference(st3))    # st1 st3 차집합 (st1 - st3)
print(st1.difference(st2).difference(st3))  # # st1 st2 st3 차집합 ((st1 - st2) - st3)

