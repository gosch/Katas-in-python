def caesarBoxCipherEncoding(inputString):
    r = []
    square = int(len(inputString) ** 0.5)
    for i in range(square):
        row = []
        for j in range(square):
            row.append(inputString[i*square+j])
        r.append(row)

    result = ''
    for i in range(square):
        for j in range(square):
            result += r[j][i]

    return result


print(caesarBoxCipherEncoding('sixteenletters16'))
