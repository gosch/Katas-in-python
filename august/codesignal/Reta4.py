def makeArrayConsecutive2(statues):
    statues = sorted(statues)
    before = statues[0]
    pending = []
    pointer = 1
    while pointer < len(statues):
        if before + 1 == statues[pointer]:
            before += 1
            pointer+1
        else:
            pending.append(before + 1)
            before += 1


    return pending


def truncateString(s):
    flag = True
    while flag:
        flag = False
        if len(s) == 0:
            return ''
        elif int(s[0]) % 3 == 0:
            s = s[1:]
            flag = True
        elif int(s[-1]) % 3 == 0:
            s = s[:-1]
            flag = True
        elif (int(s[0]) + int(s[-1])) % 3 == 0:
            s = s[1:-1]
            flag = True
    return ''.join(s)

# print(makeArrayConsecutive2([6, 2, 3, 8]))
print(truncateString('312248'))
