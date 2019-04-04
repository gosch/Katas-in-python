def cyclicString(s):
    l = len(s)

    for i in range(l):
        for j in range(l - i):
            if s in (s[j:i + 1] * l):
                return i + 1


print(cyclicString("aba"))
