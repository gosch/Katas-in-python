def order_digit(n):
    st = str(n)
    s = int(st[0])
    b = int(st[0])
    for i in range(1, len(st)):
        t = int(st[i])
        if s > t:
            s = t
        if b < t:
            b = t
    return b - s


def digitDifferenceSort(a):
    return sorted(a[::-1], key=order_digit)

print(digitDifferenceSort([152, 23, 7, 887, 243]))
