def lrSegmentNumber(l, r):
    number = []
    for i in range(l, r + 1):
        number.append(str(i))
    return ''.join(number)

print(lrSegmentNumber(2, 4))
