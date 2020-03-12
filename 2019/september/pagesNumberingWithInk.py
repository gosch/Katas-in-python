import math

def pagesNumberingWithInk(current, numberOfDigits):
    d = math.log10(current) // 1
    d += 1
    while numberOfDigits > 0:
        r = 10 ** d - current
        t = numberOfDigits
        numberOfDigits -= r * d
        current = 10 ** d if numberOfDigits > 0 else current + (t // d) - 1
        d += 1
    return current



print(pagesNumberingWithInk(8, 4))
