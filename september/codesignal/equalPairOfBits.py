
def equalPairOfBits(n, m):
    pos = 0
    while n > 0:
        if n % 2 == m % 2:
            return 2**pos
        else:
            n //= 2
            m //= 2
            pos += 1
    return 2**pos


print(equalPairOfBits(10, 11))
