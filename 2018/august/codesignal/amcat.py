def cellCompete(states, days):
    # WRITE YOUR CODE HERE

    for i in range(days):
        temp = states[:]
        for j in range(len(states)):
            if j == 0:
                if states[j + 1] == 0:
                    states[j] = 0
                else:
                    states[j] = 1
            elif j == len(states) - 1:
                if states[j - 1] == 0:
                    states[j] = 0
                else:
                    states[j] = 1
            else:
                if states[j - 1] == states[j + 1]:
                    states[j] = 0
                else:
                    states[j] = 1
    return states

import math
def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    val = math.gcd(arr[0], arr[1])
    for i in range(1, len(arr)):
        val = math.gcd(val, arr[i])
    return val

# print(cellCompete([1, 0, 0, 0, 0, 1, 0, 0], 1))
print(generalizedGCD(5, [2, 3, 4, 5, 6]))
