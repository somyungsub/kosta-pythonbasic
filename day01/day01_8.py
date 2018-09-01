# 튜플
# 모든 데이터타입을 담을 수 있음
# 한번 담으면 수정 삭제가 불가능함 (final 개념)
# 안심 안정적인 데이터 타입이 될 수 있음

a = (1, 2)
print(a)
a = (1, 2, 3, 4, 5, 6)
print(a)
a = (1, "a", 3.2, [1, 2, 5], {"2": 1, 55: 2, "b1": 4}, 6)
print(a)
print("Hello %s %s " % ('a', 'b'))  # 튜플의 예

a = (1, 2, 3, 'a', 2.0, [], (1, 2))
print(a[2])
print(a.count(1))

# 수정하고 싶거나 임의의 튜플을 수정가능하게 만들기 -> 리시트를 이용
a1 = list(a)
print(a)
print(a1)

a = tuple()
print(a)
a = tuple(a1)
print(a)
print(a[0])
