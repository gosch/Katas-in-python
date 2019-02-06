def differentDigitsNumberSearch(inputArray):
    for i in inputArray:
        s = str(i)
        c = set()
        flag = True
        for j in range(len(s)):
            if j in c:
                flag = False
                break
            else:
                c.add(j)
        if flag:
            return i

    return -1


print(differentDigitsNumberSearch([22, 111, 101, 124, 33, 30]))
