def createAnagram(s, t):
    s = sorted(s)
    t = sorted(t)

    counter = 0
    temp1 = [0] * 26
    for i in range(len(s)):
        temp1[ord(s[i]) - ord('A')] += 1
        temp1[ord(t[i]) - ord('A')] -= 1

    for i in range(26):
        if temp1[i] != 0:
            counter += 1
    return counter/2


print(createAnagram('AABAA', 'BBAAA'))
