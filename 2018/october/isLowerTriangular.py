def isLowerTriangularMatrix(matrix):
    for i in range(1, len(matrix)):
        for j in range(0, i):
            if matrix[i][j] != 0:
                return False
    return True


m = [[1,0,0],
 [4,0,0],
 [0,3,3]]

print(isLowerTriangularMatrix(m))
