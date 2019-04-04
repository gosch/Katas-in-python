def arrayChange(inputArray):
    c = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i - 1]:
            inputArray[i] = inputArray[i - 1] + 1
            c += inputArray[i - 1] - inputArray[i] + 2
    return c


print(arrayChange([1, 1, 1]))
