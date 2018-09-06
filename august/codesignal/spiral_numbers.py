def spiralNumbers(n):
    matrix = [[0 for x in range(n)] for i in range(n)]


    i = j = 0
    right = True
    down = left = up = False
    for value in range(1, n * n + 1):
        matrix[i][j] = value
        if value == n*n:
            break
        while True:
            if right:
                j += 1
                if j == n or matrix[i][j] > 0:
                    j -= 1
                    right = False
                    down = True
                else:
                    break
            elif down:
                i += 1
                if i == n or matrix[i][j] > 0:
                    i -= 1
                    left = True
                    down = False
                else:
                    break
            elif left:
                j -= 1
                if j == -1 or matrix[i][j] > 0:
                    j += 1
                    up = True
                    left = False
                else:
                    break
            elif up:
                i -= 1
                if i == -1 or matrix[i][j] > 0:
                    i += 1
                    up = False
                    right = True
                else:
                    break
            else:
                break

    return matrix

print(spiralNumbers(3))