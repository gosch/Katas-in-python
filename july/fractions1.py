from fractions import Fraction
def fractionDivision(a, b):
    up = a[0] * b[1]
    down = a[1] * b[0]
    result = str(Fraction(up, down))
    result = result.split('/')
    result = [int(result[0]), int(result[1])] if len(result) > 1 else [int(result[0]), 1]
    return result

print(fractionDivision([9, 4], [3, 4]))
