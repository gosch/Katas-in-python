def nextSecond(c):
    c[2] += 1
    if c[2] == 60:
        c[2] == 0
        c[1] += 1
        if c[1] == 60:
            c[1] = 0
            c[0] += 1
            if c[0] == 24:
                c[0] = 0
    return c


print(nextSecond([2, 3, 59]))