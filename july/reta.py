def alphabetSubstring(s):
    num = ord(s[0])
    for i in range(1, len(s)):
        n = ord(s[i])
        if num + 1 != n:
            return False

    return True

print(alphabetSubstring('efghi'))
