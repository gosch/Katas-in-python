import copy


def count(board, x, y):
    s = 0
    for i in range(y + 1, len(board[0])):
        if board[x][i] != '*':
            s = s + 1
        else:
            break
    for i in range(y - 1, -1, -1):
        if board[x][i] != '*':
            s = s + 1
        else:
            break
    for i in range(x + 1, len(board)):
        if board[i][y] != '*':
            s = s + 1
        else:
            break
    for i in range(x - 1, -1, -1):
        if board[i][y] != '*':
            s = s + 1
        else:
            break
    return s + 1





def kuromasuPuzzle(board):
    c = copy.deepcopy(board)

    for i in range(len(c)):
        for j in range(len(c[i])):

            if c[i][j] == '*' or c[i][j] == '.':
                c[i][j] = -1
            else:
                c[i][j] = count(board, i, j)
    return c


board = [["*", ".", "#", ".", ".", "*", ".", ".", "#", ".", "."],
         [".", "*", ".", ".", "*", ".", "*", ".", "#", ".", "."],
         [".", ".", ".", ".", "#", ".", ".", ".", ".", ".", "#"],
         ["#", ".", ".", ".", ".", ".", ".", "*", ".", "*", "."],
         ["*", "#", ".", ".", "*", ".", ".", ".", "*", ".", "."],
         [".", ".", "#", ".", "#", ".", "#", "*", "#", ".", "."],
         [".", ".", "*", ".", ".", ".", ".", ".", "*", "#", "*"],
         [".", ".", ".", ".", "*", ".", "*", ".", ".", "*", "#"],
         ["#", ".", "*", ".", ".", "*", "#", ".", "*", ".", "."],
         [".", ".", "#", ".", ".", ".", "*", ".", ".", ".", "."],
         [".", "*", "#", "*", ".", "*", ".", ".", "#", ".", "*"]]

print(kuromasuPuzzle(board))
