def reverseInteger(x):
    r = 0
    f = False if x < 0 else True
    x = abs(x)
    while x > 0:
        r = r * 10 + x % 10
        x = x // 10
    return r if f else -r


print(reverseInteger(-3424))
