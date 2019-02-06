def isBeautifulString(inputString):
    l = [0] * 26
    for i in inputString:
        l[ord(i) - ord('a')] += 1

    j = 0
    for i in range(26):
        if l[i] == 0:
            j = i
        else:
            break
    c = l[j]
    while j < 25 and l[j + 1] > 0:
        if l[j] < l[j + 1]:
            return False

        j += 1


    return c == len(inputString)

print(isBeautifulString("aabbb"))
