def sumUpDigits(inputString):
    res = 0
    number = ''
    flag = False
    i = 0
    while i < len(inputString):
        while i < len(inputString) and inputString[i].isdigit():
            number += inputString[i]
            i+=1
        if number.isdigit():
            res += int(number)
        number = ''
        i+=1
    return res

def reversedSumOfDigits(p, n):
    if n == 1:
        if 0 <= p <= 9:
            return str(p)
        return "-1"
    if n * 9 < p or p < 1:
        return "-1"
    s = [0] * n
    s[0] = 1
    p -= 1
    for i in reversed(range(n)):
        while s[i] < 9 and p > 0:
            s[i] += 1
            p -= 1
    return ''.join (map (str, s))


def maxSubarray(inputArray):
    for i in range(0, len(inputArray) - 1):
        s = 0
        for j in range(i, inputArray):
            s += inputArray[j]
            maxSum = max(s, maxSum)
    return maxSum

print(reversedSumOfDigits(2, 5))
