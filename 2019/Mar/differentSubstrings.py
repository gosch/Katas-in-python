def differentSubstrings(inputString):
    r = set()
    l = len(inputString)
    for i in range(l - 1, 0, -1):
        for j in range(0, l - i + 1):
            r.add(inputString[j:j + i])
    return len(r) + 1


print(differentSubstrings("abac"))
