# 예외

a = [1, 2, 3, 4, 5]

# 예외가 발생할 만한 코드 작성
def f():
    try:
        print(a[5])
    except IndexError as e:
        raise e
    finally:
        pass
    return "잘 실행됨"

f()



