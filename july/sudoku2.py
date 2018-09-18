def sudoku2(grid):
    for i in range(len(grid)):
        temp = [False for i in range(9)]
        for j in range(len(grid[i])):
            if grid[i][j] is not '.':
                if temp[int(grid[i][j]) - 1]:
                    return False
                temp[int(grid[i][j]) - 1] = True

    for i in range(len(grid)):
        temp = [False for i in range(9)]
        for j in range(len(grid[i])):
            if grid[j][i] is not '.':
                if temp[int(grid[j][i]) - 1]:
                    return False
                temp[int(grid[j][i]) - 1] = True

    for i in range(9):
        temp = [False for i in range(9)]
        for j in range(3):
            for k in range(3):
                if grid[i//3*3+j][i%3*3+k] is not '.':
                    if temp[int(grid[i//3*3+j][i%3*3+k]) - 1]:
                        return False
                    temp[int(grid[i//3*3+j][i%3*3+k]) - 1] = True

    return True


grid = [[".", ".", ".", "2", ".", ".", "6", ".", "."],
        [".", ".", ".", "1", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", "1", ".", ".", "8"],
        [".", "3", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "9", ".", ".", ".", ".", "3"],
        ["4", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "3", "8", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "4"]]

print(sudoku2(grid))
