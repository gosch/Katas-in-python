def comfortableNumbers(l, r):
    res = 0
    for i in range(l, r + 1):

        s = sum([int(j) for j in str(i)])

        if not -s <= i <= s + 1:
            res += 1

    return res


print(comfortableNumbers(10, 12))
