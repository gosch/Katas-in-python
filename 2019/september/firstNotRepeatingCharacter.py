def firstNotRepeatingCharacter(s):
    for i in range(len(s)):
        if s.rfind(s[i]) == s.find(s[i]):
            return s[i]
    return '_'

print(firstNotRepeatingCharacter("abacabaabacaba"))
