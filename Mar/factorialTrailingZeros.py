import math


def factorialTrailingZeros(n):
    n = math.factorial(n)
    c = 0
    while n > 0:
        if n % 10 == 0:
            n /= 10
            c += 1
        else:
            break
    return c


print(factorialTrailingZeros(29))