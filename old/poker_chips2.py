def pokerChips2(chips):
    moves1 = countPokerMoves(chips[:])
    moves2 = countPokerMoves(chips[::-1])
    if moves1 < moves2:
        return moves1
    return moves2

def countPokerMoves(chips):
    average = sum(chips) / len(chips)
    max_value = max(chips)
    moves = 0
    for i, chip in enumerate(chips):
        if chip == max_value:
            for j in range(len(chips)):
                if i+j == len(chips):
                    i = 0 - j
                temp = chips[i+j] - average
                if temp == 0:
                    continue
                else:
                    moves += 1
                chips[i + j] -= temp
                if i+j+1 == len(chips):
                    chips[0] += temp
                else:
                    chips[i+j+1] += temp
            break
    return moves

print(pokerChips2([13, 8, 28, 21, 30, 6, 13, 27, 23, 1]))
