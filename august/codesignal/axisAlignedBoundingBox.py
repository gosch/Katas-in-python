def axisAlignedBoundingBox(x, y):
    x = sorted(x)
    y = sorted(y)

    return (x[2] - x[0]) * (y[2] - y[0])


def lookAndSaySequenceNextElement(element):
    result = []
    selected = None
    count = 0
    i = 0
    while i < len(element):
        if element[i] == selected:
            pass
        else:
            selected = element[i]
            while i < len(element) and element[i] == selected:
                count += 1
                i += 1
            result += str(count) + str(element[i - 1])

    return ''.join(result)

x = [1, 1, 1, 10]
y = [0, -1, 1, 0]

# print(axisAlignedBoundingBox(x, y))
print(lookAndSaySequenceNextElement('1'))
