def lineEncoding(s):
    result = []
    c = s[0]
    for i in range(1, len(s)):
        if c[0] == s[i]:
            c += s[i]
        else:
            result.append(c)
            c = s[i]
    result.append(c)
    s = ''
    for i in result:
        s += str(len(i)) + i[0] if len(i) > 1 else i[0]
    return s

print(lineEncoding('aabbbc'))