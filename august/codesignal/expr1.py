class MyObject:

    def __init__(self, my_value = None):
        super()
        self.value = my_value

    def __eq__(self, other):
        print('Value ' + str(self.value))
        print('Self ' + str(self))
        print('Other ' + str(other))
        return self.value == other.value


a = MyObject('a')
b = MyObject('b')
# a = None
b = None
if a is b:
    print('1 a == b')
else:
    print('1 a != b')
print('pass')
print(not a)
if a == b:
    print('2 a == b')
else:
    print('2 a != b')


