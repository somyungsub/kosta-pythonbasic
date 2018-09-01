# 숫자
from builtins import divmod, complex

# 정수 할당
n1 = 4
n2 = 3
n3 = 2

# 실수 할당
n1 = 4.0
n2 = 3.0
n3 = 2.0

# 복소수 할당    -> 정수 나눗셈, 나머지 연산자는 안됨
# n1 = 4j
# n2 = 3j
# n3 = 2j


print(n1 + n3)
print(n1 - n3)
print(n1 / n3)
print(n1 / n2)  # 기본적으로 실수형으로 변환 후 실행되어 실수형 반환
print(n1 // n2)  # //는 정수형으로 됨
print(n1 * n3)
print(n1 % n3)
print(n1 % n3)

# 몫 + 나머지 얻기
print(divmod(n1, n2))    # 몫,나머지 튜플 형식 반환

# 정수
i1 = 5          # 초기화를 통한 방법
i2 = int(10)    # int()를 통한 방법 : i2 = 0 과 동일
print(i1)
print(i2)

# 실수
i1 = 5.0
i2 = float()    # 0.0으로 초기화됨
print(i1)
print(i2)

# 복소수
i1 = 5j
i2 = complex()  # 0j으로 초기화됨
print(i1)
print(i2)


