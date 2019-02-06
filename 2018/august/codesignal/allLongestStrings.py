def allLongestStrings(inputArray):
    r = []
    s = 0
    for i in inputArray:
        s1 = len(i)
        if s1 == s:
            r.append(i)
        elif s1 > s:
            s = s1
            s = [i]
    return s


print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))
