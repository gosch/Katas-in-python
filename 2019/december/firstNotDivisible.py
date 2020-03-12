def firstNotDivisible(divisors, start):
    flag = True
    while flag:
        flag = False
        for i in divisors:
            if start % i == 0:
                flag = True
                break
        start += 1

    return start - 1

divisors = [2, 3, 4]
start = 14


print(firstNotDivisible(divisors, start))

