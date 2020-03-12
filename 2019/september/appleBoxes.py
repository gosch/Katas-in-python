def appleBoxes(k):
    return sum([i*i for i in range(2, k+1, 2)]) - sum([i*i for i in range(1, k+1, 2)])

