def differentValuesInMultiplicationTable2(n, m):

    mat = [[0 for j in range(m)] for i in range(n)]
    r = set()
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            v = (i+1)*(j+1)
            r.add(v)
            mat[i][j] = v
    return len(r)


print(differentValuesInMultiplicationTable2(3, 2))
