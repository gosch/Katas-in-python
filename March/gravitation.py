def gravitation(rows):
    count = [-1] * len(rows[0])

    for j in range(len(rows[0])):
        for i in range(len(rows)):
            if rows[i][j] == '#' and count[j] == -1:
                count[j] = 0
            elif count[j] != -1 and rows[i][j] == '.':
                count[j] += 1

    m = min(count)

    r = []
    for i in range(len(count)):
        if count[i] == m or 0 == count[i]:
            r.append(i)
    return r


rows = ["#..#.",
        ".##..",
        ".#...",
        ".#..."]

print(gravitation(rows))
