def dfsComponentSize(matrix, vertex):
    c = set()
    u = list()
    u.append(vertex)

    e = vertex
    while u:
        u.remove(e)
        c.add(e)

        for i in range(len(matrix[e])):
            if matrix[e][i] and i not in c:
                u.append(i)

        if not u:
            break
        e = u[0]

    return len(c)


matrix = [[False, True, False], [True, False, False], [False, False, False]]

print(dfsComponentSize(matrix, 0))