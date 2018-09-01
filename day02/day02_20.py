# 예외

a = [1, 2, 3, 4, 5]

# 예외가 발생할 만한 코드 작성
try:
    1/0
    print(a[5])
except (IndexError, ZeroDivisionError) as e:
    print(e)
    print("예외가 잡힘")
finally:
    print("에러가 나든 안나든 무조건 실행되어야 하는 문장")


# Exception - 최상위

