def additionWithoutCarrying(param1, param2):
    p1 = str(param1)
    p2 = str(param2)
    r = [0] * max(len(p1), len(p2))

    for i in range(len(r)):
        r[-i-1] = str((int(p1[-i-1]) + int(p2[-i-1])) % 10 if len(p1) > i < len(p2)
                   else p1[-i-1] if len(p1) > len(p2) else p2[-i-1])
    return int(''.join(r))


print(additionWithoutCarrying(456, 1734))