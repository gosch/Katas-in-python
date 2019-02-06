def smallestUnusualNumber(a):
    num = 0
    mul = 1
    n = int(a)
    a = a.split()
    for i in range(len(a)):
        acum = int(a[i])
        num = num + acum
        mul = mul * acum
    mul = mul // int(a[-1])

    counter = 10 - n % 10

    for i in range(int(a[-1]), counter):
        if mul * i <= num:
            return str(n + i)
    return counter



print(smallestUnusualNumber("11"))