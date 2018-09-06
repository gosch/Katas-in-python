def sudoku(grid):
    for i in range(9):
        temp = [False] * 9
        for j in range(3):
            for k in range(3):
                # if grid[i//3*3+j][i%3*3+k] is not '.':
                if temp[int(grid[i // 3 * 3 + j][i % 3 * 3 + k]) - 1]:
                    return False
                temp[int(grid[i // 3 * 3 + j][i % 3 * 3 + k]) - 1] = True
    return True


grid = [[1, 3, 2, 5, 4, 6, 9, 2, 7],
        [4, 6, 5, 8, 7, 9, 3, 8, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]

print(sudoku(grid))
