def almostIncreasingSequence(sequence):
    size = len(sequence)
    if size <= 2:
        return True

    flag = False

    for i in range(size - 1):
        if sequence[i] >= sequence[i+1]:
            flag = True
            c = i
            break
    temp = [min(sequence[0], sequence[1]) - 1] + sequence[:] + [max(sequence[-1], sequence[-2]) + 1]
    c += 1
    if flag:
        if temp[c-1] < temp[c+1]:
            pass
        elif temp[c-2] > temp[c] < temp[c+1]:
            c = c-1
        elif temp[c] < temp[c+2]:
            c = c+1

    previous = 0
    for i in range(1, len(temp)):
        if i == c:
            continue
        if temp[previous] >= temp[i]:
            return False
        previous = i

    return True

# print(almostIncreasingSequence([1, 3, 2]))
print(almostIncreasingSequence([1, 2, 1, 2]))
