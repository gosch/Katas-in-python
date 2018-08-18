def isPermutation(n, inputArray):
    inputArray = sorted(inputArray)

    counter = 1
    if inputArray[-1] != n:
        return False
    for i in inputArray:
        if i != counter:
            return False
        counter += 1
    return True

print(isPermutation(3, [2, 3, 2]))
