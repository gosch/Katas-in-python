def buildPalindrome(st):
    l = len(st)
    m = l // 2
    if l % 2 == 0:
        a = m - 1
        b = m
    else:
        a = m - 1
        b = m + 1
    temp = st[:]
    count = 0
    while a >= 0:
        if temp[a] != temp[b]:
            count += 1
            temp = st[:] + "".join(list(reversed(st[:count])))
            l += 1
            m = l // 2
            if l % 2 == 0:
                a = m - 1
                b = m
            else:
                a = m - 1
                b = m + 1
        else:
            a -= 1
            b += 1
    return temp


print(buildPalindrome('abcdc'))