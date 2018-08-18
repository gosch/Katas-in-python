
def differentDigitsNumberSearch(inputArray):
    for i in inputArray:
        check = set()
        flag = True
        s = str(i)
        for j in s:
            if j in check:
                flag = False
                break
            else:
                check.add(j)
        if flag:
            return i
    return -1

print(differentDigitsNumberSearch([22, 111, 101, 124, 33, 30]))