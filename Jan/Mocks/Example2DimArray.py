

class A:
    def __init__(self, value):
        self.__v = value


class B(A):
    def __init__(self, value):
        self.__v = value


# array = [[[0] * 2] * 2] * 4
# print(array)

b = B(20)
print(b._B__v)
