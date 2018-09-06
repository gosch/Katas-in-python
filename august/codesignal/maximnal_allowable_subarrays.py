def maximalAllowableSubarrays(inputArray, maxSum):
    res = []
    l = len(inputArray)
    end = -1
    bef = 0
    suma = 0
    for i in range(l):
        suma -= bef
        bef = inputArray[i]
        if end < l:
            end += 1
            suma += inputArray[end] if end <
            while suma <= maxSum and end < l:
                end += 1
                suma += inputArray[end]


        res.append(end - 1)

    return res


inputArray = [2, 3, 0, 1, 2]
maxSum = 4
print(maximalAllowableSubarrays(inputArray, maxSum))
