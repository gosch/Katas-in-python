def rounders(n):
    c = 0
    s = len(str(n))
    for i in range(s - 1):
        c = 1 if n % 10 + c >= 5 else 0
        n //= 10
    return (n + c) * 10 ** (s-1)


print(rounders(20))

