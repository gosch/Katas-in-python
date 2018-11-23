def swapDiagonals(matrix):
    for i in range(len(matrix)):

        t = matrix[i][-1-i]
        matrix[i][-1-i] = matrix[i][i]
        matrix[i][i] = t
    return matrix

matrix = [[1,2,3],
 [4,5,6],
 [7,8,9]]

print(swapDiagonals(matrix))