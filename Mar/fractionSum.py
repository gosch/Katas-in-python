def fractionSum(a, b):
    primes = [2, 3, 5, 7, 11, 13, 17]

    r = [0, 0]
    if a[1] == b[1]:
        r[0] = a[0] + b[0]
        r[1] = a[1]

    else:
        r[1] = a[1] * b[1]
        r[0] = a[0] * b[1] + b[0] * a[1]

    flag = True
    while flag:
        flag = False
        for i in primes:
            if r[0] % i == 0 and r[1] % i == 0:
                r[0] /= i
                r[1] /= i
                flag = True

    return r


print(fractionSum([3,5], [7,5]))
