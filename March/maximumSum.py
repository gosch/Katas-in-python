
def maximumSum(a, q):
    c = [[0, i] for i in range(len(a))]
    for pair in q:
        for i in range(pair[0], pair[1] + 1):
            c[i][0] += 1

    c = sorted(c, key=lambda v: v[0], reverse=True)
    a = sorted(a, reverse=True)
    r = [0] * len(a)
    for i in range(len(a)):
        r[c[i][1]] = a[i]

    s = 0
    for pair in q:
        s += sum(r[pair[0]:pair[1] + 1])

    return s


print(maximumSum([9, 7, 2, 4, 4], [[1, 3], [1, 4], [0, 2]]))
