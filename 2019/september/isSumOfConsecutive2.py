def isSumOfConsecutive2(n):
    if n < 2:
        return False
    divisor = 2
    dif = 1
    counter = 1
    r = 0
    while n // divisor + dif <= n:
        if (n - dif) % divisor == 0:
            # print('divisor ' + str(divisor) + ' difference ' + str(dif))
            r += 1
        counter += 1
        dif += counter
        divisor += 1

    return r


def isSumOfConsecutive3(n):
    way = 0
    for i in range(1, n // 2 + 1):
        temp = 0
        j = i
        while temp < n:
            temp += j
            j += 1
        if temp == n:
            way += 1

    return way


# print(isSumOfConsecutive2(10000))
# print(isSumOfConsecutive3(10000))

for i in range(1, 10001):
    t1 = isSumOfConsecutive2(i)
    t2 = isSumOfConsecutive3(i)
    if t1 != t2:
        print("Difference in " + str(i))
    if i % 100 == 0:
        print("Count " + str(i))
