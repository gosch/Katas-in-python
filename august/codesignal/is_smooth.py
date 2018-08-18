def isSmooth(arr):
    s = len(arr)
    if s % 2 == 0:
        return arr[s-1] == arr[0] == (arr[s//2] + arr[s//2 - 1])
    else:
        return arr[s-1] == arr[0] == (arr[s//2])


def isDiagonalMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                continue
            if matrix[i][j] != 0:
                return False

    return True


import re


def longestDigitsPrefix(inputString):
    num = ''
    biggest = ''
    flag = False

    for i in re.split("[^0-9]+", inputString):
        if len(i) > biggest:
            biggest = inputString[i]

    return biggest
# print(isSmooth([7, 2, 2, 5, 10, 7]))
print(isDiagonalMatrix([[1, 0, 0],
                        [0, 5, 0],
                        [0, 0, 3]]))
