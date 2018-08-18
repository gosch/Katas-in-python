def boxBlur(image):
    r = []

    for i in range(1, len(image) - 1):
        row = []
        for j in range(1, len(image[i]) - 1):
            top = image[i - 1][j - 1:j + 2]
            down = image[i + 1][j - 1:j + 2]
            ave = sum(top + [image[i][j - 1]] + [image[i][j + 1]] + down + [image[i][j]])
            ave = ave // 9
            row.append(ave)
        r.append(row)
    return r


image = [[1, 1, 1],
         [1, 7, 1],
         [1, 1, 1]]
print(boxBlur(image))
