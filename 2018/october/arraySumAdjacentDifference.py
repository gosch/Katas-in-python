def arraySumAdjacentDifference(inputArray):
    dif = 0
    for i in range(len(inputArray) - 1):
        dif = abs(max(inputArray[i], inputArray[i+1]) - min(inputArray[i], inputArray[i+1]))
    return dif

print(arraySumAdjacentDifference([4, 7, 1, 2]))