def specialPolynomial(x, n):
    r = 0
    i = 0
    while r <= n:
        r += x**i
        i += 1
    return i - 1


print(specialPolynomial(2, 5))
