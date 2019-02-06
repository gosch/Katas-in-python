import itertools


def is_valid(a, b):
    if a == b:
        return False
    count = 0
    for x, y in zip(a, b):
        if x != y:
            count += 1
        if count > 1:
            break
    if count == 1:
        return True
    return False


def stringsRearrangement(inputArray):
    all_com = itertools.permutations(inputArray)
    all_com = [i for i in all_com]
    for com in all_com:
        i = 0
        flag = True
        while i < len(com)-1:
            if not is_valid(com[i], com[i + 1]):
                flag = False
                break
            i += 1
        if flag:
            return True
    return False

inputArray = ["ab", "bb", "aa"]

print(stringsRearrangement(inputArray))

