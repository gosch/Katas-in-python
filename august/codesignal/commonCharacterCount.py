def commonCharacterCount(s1, s2):
    counter = [0] * 26
    counter2 = [0] * 26
    r = 0
    a = ord('a')
    for i in s1:
        counter[ord(i) - a] += 1
    for i in s1:
        counter2[ord(i) - a] += 1
    for i in range(len(counter)):
        if counter[i] > 0 and counter2[i] > 0:
            r += min(counter[i], counter2[i])
    return r