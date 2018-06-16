def pokerChips2(chips):
    memory = {}
    total = len(chips)
    return count_poker_moves(chips, 0, sum(chips) / len(chips), total, memory)

def count_poker_moves(chips, moves, average, total, memory):
    str_value = ''
    max_value = max(chips)
    position = chips.index(max_value)
    new_chips = chips[position:position+1] + chips[position+1:] + chips[:position]

    for value in map(lambda x: str(x), new_chips):
        str_value += value + ','

    if str_value in memory:
        return memory[str_value]

    if max_value == average or moves == total:
        return moves

    new_array = new_chips[1:]
    new_array2 = new_array[:]
    new_array[0] += max_value - average
    new_array2[len(new_array2)-1] += max_value - average
    count1 = count_poker_moves(new_array, moves, average, total, memory)
    count2 = count_poker_moves(new_array2, moves, average, total, memory)

    if count1 < count2:
        total_moves = moves + count1 + 1
    else:
        total_moves = moves + count2 + 1
    memory[str_value] = total_moves
    return total_moves

print(pokerChips2([18, 22, 30, 21, 2, 20, 22, 8, 30, 30, 7, 23, 1, 22, 8, 23, 7, 22, 25, 26, 17, 30, 27, 6, 25, 29, 20, 9, 3, 25, 16, 16, 30, 30, 8, 15, 27, 25, 6, 22, 16, 10, 24, 14, 26, 0, 13, 28, 11, 5]))
