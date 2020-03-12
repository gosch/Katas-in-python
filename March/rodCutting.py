def rodCutting(n, v):
    # v = v[1:]
    val = [0] * len(v)

    for i in range(1, n + 1):
        mv = -99999
        for j in range(i):
            mv = max(mv, v[j] + val[i-j-1])
        val[i] = mv
    return val[n]


def rodCutting2(n, v):

    if n <= 0:
        return v[0]

    mv = -99999
    for i in range(1, n + 1):
        mv = max(mv, v[i] + rodCutting2(n - i, v))
    return mv


print(rodCutting(25, [0, 4, 10, 19, 19, 28, 32, 39, 41, 51, 57, 61, 61, 71, 76, 77, 83, 85, 88, 95, 98, 103, 108, 113, 118, 121]))
