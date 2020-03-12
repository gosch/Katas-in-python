def createAnagram(s, t):
    s1 = {}
    s2 = {}
    r = 0

    for i in s:
        if i in s1:
            s1[i] += 1
        else:
            s1[i] = 1
    for i in t:
        if i in s2:
            s2[i] += 1
        else:
            s2[i] = 1

    for k, v in s1.items():
        if k in s2:
            r += abs(s1[k] - s2[k])
            del s2[k]
        else:
            r += v

    for i in s2.values():
        r += i
    return r//2


print(createAnagram("AABAA", "BBAAA"))
