
def isoscelesTriangle(sides):
    sides.sort()
    if sides[1] == sides[2]:
        return True
    else:
        return False


print(isoscelesTriangle([5, 3, 5]))
