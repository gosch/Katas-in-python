def kbonacci(k, n):
    b = c = k
    c = n % k + 1 if n < k else c
    p = [1 for _ in range(k)]
    for i in range(k, n):
        t = i % k
        c = c - p[t] + b
        p[t] = b
        b = c
    return str(c)

print(kbonacci(16, 100_000))
