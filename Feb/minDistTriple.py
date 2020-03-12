def minDistTriplet(a, b, c):

    i = j = k = 0
    d = a[-1] + b[-1] + c[-1]

    while i < len(a) and j < len(b) and k < len(c):

        mi = min(a[i], min(b[j], c[k]))
        ma = max(a[i], max(b[j], c[k]))

        if ma - mi < d:
            ri = i
            rj = j
            rk = k
            d = ma - mi

        if d == 0:
            break
        if a[i] == mi:
            i += 1
        elif b[j] == mi:
            j += 1
        else:
            k += 1

    return abs(a[ri] - c[rk]) + abs(a[ri] - b[rj]) + abs(b[rj] - c[rk])


a = [20, 34, 74, 75]
b = [18, 20, 30, 32, 40, 65, 92, 94]
c = [0, 0, 15, 60, 60, 72, 76, 86, 96]


print(minDistTriplet(a, b, c))