def alphabetSubsequence(s):
    initial = 0
    for i in s:
        if ord(i) <= initial:
            return False
        else:
            initial = ord(i)
    return True


print(alphabetSubsequence('effg'))
