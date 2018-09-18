def specialPolynomial(x, n):
    pol = 0
    r = 0
    while r <= n:
        r += x**pol
        pol+=1
    return pol


print(specialPolynomial(2, 5))
