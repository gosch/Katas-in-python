def firstMultiple2(divisors, start):
    maxi = 1
    for i in divisors:
        maxi *= i
    for i in range(start, maxi+1):

        for j in divisors:
            if j % i == 0:
                return i

    return 0

print(firstMultiple2([1], 123))