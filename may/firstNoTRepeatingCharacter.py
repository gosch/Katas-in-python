def firstNotRepeatingCharacter(s):
    non_repeated = '_'
    for c in range(len(s)):
        non_repeated = s[c]
        for i in range(len(s)):
            if c == i:
                continue
            if s[i] == non_repeated:
                non_repeated = '_'
                break
        if non_repeated != '_':
            break
    return non_repeated

print(firstNotRepeatingCharacter('abacabaabacaba'))