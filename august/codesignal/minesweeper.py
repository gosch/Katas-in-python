def minesweeper(matrix):
    res = []
    top = [False] * (len(matrix[0]) + 2)
    down = top[:]
    matrix_temp = []
    matrix_temp.append(top)
    for i in matrix:
        matrix_temp.append([False] + i[:] + [False])
    matrix_temp.append(down)

    for i in range(1, len(matrix_temp) - 1):
        row = []
        for j in range(1, len(matrix_temp[i]) - 1):
            up = [1 for x in matrix_temp[i - 1][j - 1:j + 2] if x]
            mid = [1 if matrix_temp[i][j-1] else 0, 1 if matrix_temp[i][j+1] else 0]
            dow = [1 for x in matrix_temp[i + 1][j - 1:j + 2] if x]
            row.append(sum(up + mid + dow))
        res.append(row)
    return res


matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]
print(minesweeper(matrix))
val = str('H')

