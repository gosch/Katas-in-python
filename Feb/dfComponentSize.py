def checkElements(matrix, n):
    new_elements = set()
    for i in n:
        size = len(matrix[i])
        n2 = [j for j in range(size) if (matrix[i][j] and j not in n)]
        new_elements.update(n2)
    if len(new_elements) == 0:
        return list(set(n))
    else:
        n.extend(list(new_elements))
        return checkElements(matrix, n)


def dfsComponentSize(matrix, vertex):
    nodes = [i for i in range(len(matrix[vertex])) if matrix[vertex][i]]
    nodes.append(vertex)
    return len(checkElements(matrix, nodes))


# m = [[False, True, False],
#      [True, False, False],
#      [False, False, False]]
m = [[False, True, False, True],
     [True, False, False, False],
     [False, False, False, False],
     [True, False, False, False]]

print(dfsComponentSize(m, vertex=1))