def maximizeNumberRoundness(n):
    st = [x for x in str(n)]
    s = len(st)
    j = s - 1
    c = 0
    for i in range(s):
        if st[i] == '0':
            while i < j and st[j] == '0':
                j -= 1
            if i == j:
                return c
            else:
                t = st[j]
                st[j] = st[i]
                st[i] = t
                c += 1
    return c


print(maximizeNumberRoundness(902200100))
