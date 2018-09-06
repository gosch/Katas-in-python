def stringsCrossover(inputArray, result):
    # elements = set()
    # for i in result:
    #     elements.add(i)

    count = 0
    positions = [False] * len(inputArray)

    for i in range(len(result)):
        letters = [x[i] for x in inputArray]
        if result[i] in letters:
            count += 1
    return count


print(stringsCrossover(['abc', 'aaa', 'aba', 'bab'], 'bbb'))
