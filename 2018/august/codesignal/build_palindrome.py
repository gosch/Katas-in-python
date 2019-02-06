def buildPalindrome(st):
    l = len(st)
    mid = l // 2
    if l % 2 == 0:
        a = mid-1
        b = mid
    else:
        a = mid - 1
        b = mid + 1
    temp = st[:]
    count = 0
    while a >= 0:
        if temp[a] != temp[b]:
            count += 1
            temp = st[:] + "".join(list(reversed(st[:count])))
            l += 1
            mid = l//2
            if l % 2 == 0:
                a = mid-1
                b = mid
            else:
                a = mid - 1
                b = mid + 1
        else:
            a-=1
            b+=1
    return temp


print(buildPalindrome('abcdc'))