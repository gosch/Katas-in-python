def isSkewSymmetricMatrix(matrix):
    if len(matrix) == 1:
        return False

    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            if matrix[i][j] != -matrix[j][i]:
                return False
    return True

matrix = [[0,0,1],
 [0,0,-2],
 [-1,-2,0]]

print(isSkewSymmetricMatrix(matrix))