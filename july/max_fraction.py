def maxFraction(numerators, denominators):
    maximum = 0
    p = -1
    for i in range(len(numerators)):
        r = numerators[i] / denominators[i]
        if r > maximum:
            
            p = i

    return p

print(maxFraction([1, 2, 3, 10],[1, 3, 4, 11]))
