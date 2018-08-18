def matrixElementsSum(matrix):
    col = []
    cost = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j in col:
                continue
            if matrix[i][j] == 0:
                col.append(j)
            else:
                cost+=matrix[i][j]
    return cost

matrix = [[0,1,1,2],
 [0,5,0,0],
 [2,0,3,3]]

print(matrixElementsSum(matrix))
