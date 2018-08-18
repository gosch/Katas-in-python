import math
def pagesNumbering(n):

    power = 1
    digits_number = 1
    result = 0

    while power * 10 <= n:
        result += power * 9 * digits_number
        power *= 10
        digits_number += 1

    result += (n - power + 1) * digits_number

    return result

print(pagesNumbering(11))
