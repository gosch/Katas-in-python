def directionOfReading(numbers):
    a = len(numbers)
    square = []
    for i in numbers:
        number = str(i).zfill(a)
        square.append(number)

    r = []
    rows = len(square)
    columns = len(square[0])
    for i in range(columns):
        val = []
        for j in range(rows):
            val.append(square[j][i])
        r.append(int(''.join(val)))
    return r


print(directionOfReading([12, 345, 67, 5]))
