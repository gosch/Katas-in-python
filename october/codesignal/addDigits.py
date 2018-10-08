def addDigits(a, b, n):
    count = 0
    while count < n:
        t = a * 10 + 9
        r = t % b
        mult = False
        c2 = 0
        while t % b != 0 and t % 10 != 0:

            t -= 1
            c2 += 1
        if t % b == 0:
            a = t
        else:
            break
        count += 1
    return str(a)


print(addDigits(4, 13, 10))
