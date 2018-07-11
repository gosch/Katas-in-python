from timeit import timeit

counter = 0


def pokerChips2(chips):
    total = len(chips)
    memory = {'best': total}
    count_poker_moves(chips, 0, sum(chips) / len(chips), total, memory)
    return memory['best']


def count_poker_moves(chips, level, average, array_size, memory):
    global counter
    counter += 1
    if level >= memory['best']:
        return array_size
    str_value = ''
    position = -1
    flag = True

    for i in range(len(chips)):
        str_value += str(chips[i]) + ','
        if flag:
            if chips[i] > average:
                position = i
                flag = False

    if flag:
        print('New best ' + str(level))
        memory['best'] = level
        return level
    if level == memory['best']:
        return array_size

    if str_value in memory:
        return memory[str_value]

    new_array1 = chips[:]
    new_array2 = chips[:]


    before = len(new_array1) - 1 if position == 0 else position - 1
    next = 0 if position + 1 == len(new_array1) else position + 1

    new_array1[before] += chips[position] - average
    new_array2[next] += chips[position] - average
    chips[position] = average
    count1 = count_poker_moves(new_array1, level + 1, average, array_size, memory)
    count2 = count_poker_moves(new_array2, level + 1, average, array_size, memory)

    if count1 < count2:
        total_moves = count1
    else:
        total_moves = count2
    memory[str_value] = total_moves
    return total_moves

start = timeit()
print(pokerChips2([22, 2, 16, 11, 10, 16, 18, 27, 20, 9, 17, 24, 26, 5, 3, 2, 22, 6, 22, 26, 7, 3, 10, 23, 0, 17, 11, 29, 9, 6, 16, 5, 25, 3, 8, 14, 17, 0, 22, 16, 29, 17, 2, 4, 18, 1, 15, 17, 15, 19, 6, 6, 15, 14, 9, 14, 30, 19, 28, 4, 9, 18, 18, 1, 7, 4, 23, 1, 24, 15, 4, 1, 3, 28, 20, 20, 21, 0, 12, 26, 8, 17, 10, 29, 5, 9, 6, 2, 12, 7, 15, 18, 10, 16, 25, 30, 26, 7, 27, 39]))

# print(pokerChips2([18, 22, 30, 21, 2, 20, 22, 8, 30, 30, 7, 23, 1, 22, 8, 23, 7, 22, 25, 26, 17, 30, 27, 6, 25, 29, 20, 9, 3, 25, 16, 16, 30, 30, 8, 15, 27, 25, 6, 22, 16, 10, 24, 14, 26, 0, 13, 28, 11, 5]))
# print(pokerChips2[48, 21, 11, 32, 19, 19, 38, 44, 36, 48, 35, 29, 44, 3, 2, 11, 19, 50, 4, 16, 5, 50, 23, 2, 1, 25, 2, 23, 0, 3, 5, 12, 8, 28, 23, 39, 49, 24, 48, 38, 38, 14, 38, 24, 6, 6, 24, 31, 32, 45, 0, 4, 39, 17, 36, 34, 35, 39, 25, 37, 11, 41, 29, 14, 1, 11, 0, 11, 25, 44, 30, 20, 23, 35, 40, 5, 12, 2, 48, 21, 46, 3, 18, 6, 45, 12, 43, 7, 23, 32, 15, 40, 50, 44, 24, 3, 49, 48, 40, 25, 21, 39, 18, 9, 30, 27, 33, 43, 15, 39, 47, 35, 13, 40, 47, 4, 22, 23, 44, 50, 10, 49, 49, 49, 30, 37, 41, 22, 6, 42, 26, 12, 19, 28, 16, 43, 35, 1, 13, 1, 49, 33, 38, 7, 46, 38, 10, 6, 40, 48])
end = timeit()
print('Time ' + str(end-start))
print(counter)
