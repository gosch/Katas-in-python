def isSum(value):
    r = 0
    c = 1
    while r < value:
        r += c
        c += 1
    return r == value


print(isSum(10))