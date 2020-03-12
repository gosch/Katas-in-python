def comfortableNumbers(l, r):

    n = []
    c = 0
    for i in range(l, r + 1):
        s = sum([int(j) for j in str(i)])
        n.append(s+i)
        if i > l:
            j = i-1
            while j >= l and j >= i - s:
                if n[j-l] >= i:
                    c += 1
                j -= 1

    return c


print(comfortableNumbers(10, 12))
