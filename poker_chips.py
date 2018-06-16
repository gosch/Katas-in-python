import numpy as np


def pokerChips(chips):
    avg = sum(chips) / len(chips)
    overflow_values = []
    overflow = 0
    for x in chips:
        overflow += x - avg
        overflow_values.append(overflow)
    overflow_median = int(np.median(overflow_values))
    res = 0
    other = 0
    print(avg)
    print(overflow_median)
    print(overflow_values)
    for i in range(len(overflow_values)):
        res += abs(overflow_values[i] - overflow_median)
        other += 0 if abs(overflow_values[i] - overflow_median) == 0 else 1
        if i != len(overflow_values) - 1:
            other += 0 if overflow_values[i] != 0 else - 1
            other += 0 if overflow_values[i] != overflow_values[i+1] else - 1
    print(other)
    return res


# print(pokerChips(
#     [22, 2, 16, 11, 10, 16, 18, 27, 20, 9, 17, 24, 26, 5, 3, 2, 22, 6, 22, 26, 7, 3, 10, 23, 0, 17, 11, 29, 9, 6, 16, 5,
#      25, 3, 8, 14, 17, 0, 22, 16, 29, 17, 2, 4, 18, 1, 15, 17, 15, 19, 6, 6, 15, 14, 9, 14, 30, 19, 28, 4, 9, 18, 18, 1,
#      7, 4, 23, 1, 24, 15, 4, 1, 3, 28, 20, 20, 21, 0, 12, 26, 8, 17, 10, 29, 5, 9, 6, 2, 12, 7, 15, 18, 10, 16, 25, 30,
#      26, 7, 27, 39]))
pokerChips([4, 5, 6, 10, 5]) # -1
print('\n')
pokerChips([0, 10, 0, 8, 3, 10, 7, 0, 9, 3]) # -2
print('\n')
pokerChips([13, 8, 28, 21, 30, 6, 13, 27, 23, 1]) # -2
print('\n')
pokerChips([6, 14, 22, 12, 6, 25, 15, 14, 29, 21, 11, 14, 25, 13, 13]) # -1
print('\n') # -1
pokerChips([18, 22, 30, 21, 2, 20, 22, 8, 30, 30, 7, 23, 1, 22, 8, 23, 7, 22, 25, 26, 17, 30, 27, 6, 25, 29, 20, 9, 3, 25, 16, 16, 30, 30, 8, 15, 27, 25, 6, 22, 16, 10, 24, 14, 26, 0, 13, 28, 11, 5])


# print(pokerChips([6, 2, 4, 10, 3]))
# print(pokerChips([0, 10, 0, 8, 3, 10, 7, 0, 9, 3]))

