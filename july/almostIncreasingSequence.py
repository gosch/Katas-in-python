def almostIncreasingSequence(sequence):
    if len(sequence) <= 2:
        return True
    counter = 0
    for i in range(len(sequence) - 2):
        if sequence[i] >= sequence[i + 1] or sequence[i] >= sequence[i+2]:
            counter += 1
            if i-1 >= 0:
                if sequence[i-1] >= sequence[i+1] or sequence[i-1] >= sequence[i+2]:
                    return False
                else:
                    sequence[i] = sequence[i-1]

            if counter == 2:
                return False
    return True


print(almostIncreasingSequence([1, 2, 5, 3, 5]))
print(almostIncreasingSequence([10, 1, 2, 3, 4, 5]))
print(almostIncreasingSequence([1, 2, 3, 4, 3, 6]))
print(almostIncreasingSequence([1, 2, 1, 2]))
print(almostIncreasingSequence([1, 1, 1, 2, 3]))
