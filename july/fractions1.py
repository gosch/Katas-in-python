from fractions import Fraction
def fractionDivision(a, b):
    up = a[0] * b[1]
    down = a[1] * b[0]
    result = str(Fraction(up, down))
    result = result.split('/')
    result = [int(result[0]), int(result[1])] if len(result) > 1 else [int(result[0]), 1]
    return result


def fractionSum(a, b):
    r = [0, 0]
    primes = [2, 3, 5, 7, 11, 13, 17]
    if a[1] != b[1]:
        r[1] = a[1] * b[1]
        r[0] = a[0] * b[1] + b[0] * a[1]
    else:
        r[1] = a[1]
        r[0] = a[0] + b[0]

    condition = True
    while condition:
        condition = False
        for i in primes:
            if r[0] % i == 0 and r[1] % i == 0:
                r[0] //= i
                r[1] //= i
                condition = True
                break
    return r

print(fractionDivision([9, 4], [3, 4]))
