

# str -> repr
class A:
    def __repr__(self):
        return '<Class A> 이 메서드는 본연의 내용을 가지고 있습니다.'

    def __str__(self):
        return '이 클래스는 str 클래스가 호출될 때 사용됩니다.'

    def __bytes__(self):
        return b'hahaha'

    def __int__(self):
        return 1

    def __float__(self):
        return 1.0

    def __complex__(self):
        return 1j

    def __iter__(self):
        for item in range(10):
            yield item

    def __dir__(self):
        return []

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __bool__(self):
        return False

    def __hash__(self):
        return hash(123)

class B:
    def __hash__(self):
        return 4567


a = A()
b = B()
c = '111'
d = '111'
print(hash(c) == hash(d))

print(a)            # __str__ or __repr__
print(repr(a))      # __repr__
print(str(a))       # __str__


# byte
a = A()
print(bytes(a))
print(tuple(a))
print(set(a))


print(bool(a))  # not None 이므로

