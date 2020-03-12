def commonCharacterCount2(s):
    c = [[0 for _ in range(26)] for _ in range(len(s))]

    for i in range(len(s)):
        for j in s[i]:
            c[i][ord(j) - ord('a')] += 1

    r = 0
    for i in range(26):
        m = 1000
        for j in range(len(s)):
            m = min(m, c[j][i])
        if m == 0:
            continue
        else:
            r += m
    return r


t = ["aabcc", "adcaa", "acdba"]
print(commonCharacterCount2(t))
