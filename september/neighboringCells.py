def neighboringCells(matrix):
    r1 = 0
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return 0
    elif len(matrix) == 1:
        r1 = 1
    elif len(matrix[0]) == 1:
        r1 = 1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            col = 1 if 0 < i < len(matrix) - 1 else 0
            row = 1 if 0 < j < len(matrix[i]) - 1 else 0
            matrix[i][j] = 2 + col + row - r1
    return matrix


matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

matrix = [[0],
          [0],
          [0],
          [0]]
print(neighboringCells(matrix))
