def str237(s):
    v = [0]*10+[1]
    for i in s:
        n = 0
        for u in v[i:]:
            v[n] += u
            n += 1
    return v[0]

print(str237([1, 2, 3, 4, 5]))
