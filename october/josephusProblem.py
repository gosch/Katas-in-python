def josephusProblem(n, k):
    r = [True] * n

    i = 0
    c = 0
    t = n
    while n > 0:
        if r[i]:
            c += 1
            if c == k:
                r[i] = False
                n -= 1
                c = 0
        if n == 0:
            break
        i = i + 1 if i + 1 < t else 0
    return i + 1


print(josephusProblem(3, 2))

