def makeArrayConsecutive2(statues):
    statues.sort()
    count = 0
    before = statues[0]
    i = 1
    while i < len(statues):
        if before + 1 != statues[i]:
            count = count + 1

        else:
            i += 1
        before = before + 1

    return count

print(makeArrayConsecutive2([6, 2, 3, 8]))
