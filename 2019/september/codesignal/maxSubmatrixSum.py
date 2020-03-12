def calculate(matrix, x_start,x_end, y_start, y_end):
    total = 0
    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            total += matrix[i][j]
    return total

def maxSubmatrixSum(matrix, n, m):
    max_s = 0

    for i in range(len(matrix) - (n-1)):
        for j in range(len(matrix[i]) - (m-1)):
            max_s = max(max_s, calculate(matrix, i, i+n, j, j+m))
    return max_s


matrix = [[1, 12, 11, 10],
          [4,  3,  2,  9],
          [5,  6,  7,  8]]
print(maxSubmatrixSum(matrix, 2, 1))