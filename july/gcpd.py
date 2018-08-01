import math
def greatestCommonPrimeDivisor(a, b):
    bigger = a if a >= b else b
    found = -1
    primes = [2]
    for i in range(2, int(round(math.sqrt(bigger)))):
        flag = False
        for j in primes:
            if i % j == 0:
                flag = True
        if flag:
            continue
        else:
            primes.append(i)
        if a % i == 0 and b % i == 0:
            found = i
    return found

print(greatestCommonPrimeDivisor(100, 140))