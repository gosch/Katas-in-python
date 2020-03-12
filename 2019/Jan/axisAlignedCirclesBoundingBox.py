def axisAlignedCirclesBoundingBox(x, y, r):
    x_values = []

    for i in range(len(x)):
        x_values.append(x[i] - r[i])
        x_values.append(x[i] + r[i])

    y_values = []
    for i in range(len(y)):
        y_values.append(x[i] - r[i])
        y_values.append(x[i] + r[i])

    return (max(x_values) - min(x_values)) * (max(y_values) - min(y_values))


print(axisAlignedCirclesBoundingBox([1, 0, 4], [-1, 2, 2], [3, 5, 4]))
