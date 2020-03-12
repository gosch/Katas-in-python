def firstNotRepeatingCharacter(s):
    v = [0] * 26
    for i in s:
        v[ord(i) - ord('a')] += 1

    for i in s:
        if v[ord(i) - ord['a']] == 1:
            return i
    return '_'


print(firstNotRepeatingCharacter("abacabad"))