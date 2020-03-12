def maxSumSegments(inputArray):
    r = []
    r.append(inputArray.index(max(inputArray)))
    s = 2

    while s <= len(inputArray):
        t = [sum([inputArray[i + j] for j in range(s)]) for i in range(len(inputArray) - s + 1)]
        r.append(t.index(max(t)))
        s += 1
    return r


print(maxSumSegments([-1, 2, 1, 3, -2]))
