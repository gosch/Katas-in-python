def reversedSumOfDigits(p, n):
    if n <= 1:
        return str(p) if p <= 9 else str(-1)
    if p == 0:
        return str(-1)

    r = ['0' for _ in range(n)]
    r[0] = "1"
    p -= 1
    pos = n - 1

    while p > 9 and pos > 0:
        r[pos] = '9'
        p -= 9
        pos -= 1
    if p > 9:
        return str(-1)
    if pos == 0:
        p += 1

    if p >= 1:
        r[pos] = str(p)

    return ''.join(r)


print(reversedSumOfDigits(10, 3))