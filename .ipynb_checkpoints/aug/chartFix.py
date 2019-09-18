def chartFix(chart):
    rem = []
    for i in range(len(chart)):
        c = i

        for j in range(i):
            if chart[j] < chart[i]:
                c = min(c, rem[j] - 1 + i - j)
        rem.append(c)

    return c


print(chartFix([3, 2, 6, 4, 5, 1, 7]))
