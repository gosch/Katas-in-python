def arrayConversion(inputArray):
    a = inputArray[:]
    flag = True
    while len(a) > 1:
        temp = []
        for i in range(0, len(a), 2):
            temp.append(a[i] + a[i+1]) if flag else temp.append(a[i] * a[i+1])
        flag = not flag
        a = temp[:]
    return a[0]


print(arrayConversion([1, 2, 3, 4, 5, 6, 7, 8]))
