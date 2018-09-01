# iter (반복자)


# 반복자가 아니다!
a = [1, 2, 3, 4, 5]
# print(next(a))

# i = iter(a)
# print(next(i))


class yrange:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < 5:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()   # 예외 발생 -> 더 이상 반복되는 걸 막음


c = yrange()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))


def foo():
    print("begin")
    for i in range(3):
        print("before yield", i)
        yield i
        print("after yield", i)
    print("end")


for i in foo():
    print("main for")
    print(i)
    print("main for end")



