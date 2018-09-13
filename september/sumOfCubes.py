def sumOfCubes(n):
    r = 0
    for i in range(1, n):
        r += i**3
    return r

print(sumOfCubes(3))