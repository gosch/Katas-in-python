def chessKnight(cell):
    x = ord(cell[0]) - ord('a')
    y = int(cell[1]) - 1
    moves = 0

    if x + 2 < 8 and y + 1 < 8:
        moves += 1
    if x + 1 < 8 and y + 2 < 8:
        moves += 1
    if x - 1 >= 0 and y + 2 < 8:
        moves += 1
    if x - 2 >= 0 and y + 1 < 8:
        moves += 1
    if x - 2 >= 0 and y - 1 >= 0:
        moves += 1
    if x - 1 >= 0 and y - 2 >= 0:
        moves += 1
    if x + 1 <= 8 and y - 2 >= 0:
        moves += 1
    if x + 2 <= 8 and y - 1 >= 0:
        moves += 1
    return moves

print(chessKnight('g6'))