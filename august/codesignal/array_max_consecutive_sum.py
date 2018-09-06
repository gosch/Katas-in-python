def arrayMaxConsecutiveSum(inputArray, k):
    max_val = sum(inputArray[:k])
    val = max_val
    for i in range(k, len(inputArray)):
        val -= inputArray[i - k]
        val += inputArray[i]
        if max_val < val:
            max_val = val

    return max_val

print(arrayMaxConsecutiveSum([2, 3, 5, 1, 6], 2))
