def applesDistribution(apples, boxCapacity, maxResidue):
    if boxCapacity == 0:
        return 0
    counter = 1
    for i in range(2, boxCapacity+1):
        if apples % i <= maxResidue:
            counter += 1
    return counter

print(applesDistribution(7, 4, 1))
