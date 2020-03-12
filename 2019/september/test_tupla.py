
def funct(x, y, z):
    x += 1
    y += 1
    z += 1
    return x, y, z


a, b, c = 1, 2, 3
a, b, c = funct(a, b, c)
print(a)
print(b)
print(c)
