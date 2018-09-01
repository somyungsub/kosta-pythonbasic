# 리스트  모든종류의 객체와 타입을 담을 수 있음
l1 = []  # list()
print(l1)
l1.append(10)
l1.append("aa")
l1.append(10.2)
l1.append(True)
print(l1)

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l1)
print(l2)
print(l1 == l2)  # 자바와다르게 값을 가지고 비교를 하기 떄문에 True

print(l1[0:4])  # 특정범위를 가져오기
print(l1[1])
print(l1[-1])

l1[0] = 'A'
l1[-1] = 'B'
print(l1)

l1[2:6] = "bcdefg"  # 3,4,5,6 -> bcdefg를 순차적으로 삽입
print(l1)
l1[2:6] = ["bcdefg"]  # 3,4,5,6 -> bcdefg를 3의 자리에 통으로 삽입
print(l1)
l1[2:6] = [101, 205, 55]  #
print(l1)
l1[0:1] = [10, 20, 50]
print(l1)

print(l1.pop())
print(l1.pop())
print(l1.pop())
print(l1.pop())
print(l1.pop())
print(l1.pop())
print(l1)
print(l1.append(1))
print(l1.append(2))
print(l1.append(10))
print(l1)
print(l1.pop(0))  # 첫번째인자를 빼옴
print(l1.pop(0))  # 첫번째인자를 빼옴
print(l1.pop(0))  # 첫번째인자를 빼옴
print(l1)

# 하지만 주소는 다르게 배정됨
print(id(l1))
print(id(l2))

print("-------------------------------------------")
l1 = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
print(l1.count(3))
print(l1)
print(l1.remove(2))  # remove는 제거만하고 제거된 대상을 반환하지 않음
print(l1)
print(l1.remove(3))  # 처음꺼 3 1개만 지움
print(l1)

l1 = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
print(l1.index(1))
print(l1.index(3))  # 처음 찾은 index 위치를 반환함
print(l1.index(10))
# print(l1.index(15))     # ValueError 예외 발생

# del 키워드 활용
del l1[0]  # 0번째 데이터 삭제
print(l1)

del (l1[1:3])  # 한꺼번 삭제가능
print(l1)

# insert    index 위치에 데이터 삽입
l1 = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
l1.insert(0, 'a')
print(l1)
l1.insert(0, 'a1')
print(l1)
l1.insert(0, 'a2')
print(l1)

print("--------------------------------------")
# 리스트 복제
l2 = l1[:]  # 깊은복사
print(l2)
print(id(l1))
print(id(l2))
l2 = l1.copy()
print(l2)
print(id(l1))
print(id(l2))

l1.clear()  # 데이터 비우기
print(l1)

# sort  정렬
l1 = [2, 1, 5, 10, 4]
l1.sort()       # 오름차순
print(l1)
l1.reverse()    # 내림차순   == l1.sort(reverse = True)
print(l1)

l1 = sorted([2, 1, 5, 10, 4])
print(l1)
l1 = reversed([2, 1, 5, 10, 4])
print(l1)

l1 = [2, 1, 5, 10, 4]
l2 = [21, 51, 25, 101, 24]

print(l1 + l2)
print(l1)
print(l2)

# l1 확장하기
l1.extend(l2)
print(l1)
print(l2)
