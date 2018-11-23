def allLongestStrings(inputArray):
    elements = []
    max_size = 0
    for i in inputArray:
        if len(i) > max_size:
            elements = []
            elements.append(i)
            max_size = len(i)
        else:
            if len(i) == max_size:
                elements.append(i)
    return elements

print(allLongestStrings(['aba', 'abaa', 'ab']))