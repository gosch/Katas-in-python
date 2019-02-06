def optimalUtilization(deviceCapacity, foregroundAppList, backgroundAppList):
    # WRITE YOUR CODE HERE
    back = {}
    found = []
    for i in range(len(backgroundAppList)):
        if backgroundAppList[i][1] in back:
            back[backgroundAppList[i][1]].append(i + 1)
        else:
            back[backgroundAppList[i][1]] = [i + 1]

    flag = False
    for i in range(deviceCapacity, 0, -1):
        for j in range(len(foregroundAppList)):
            if (i - foregroundAppList[j][1]) in back:
                flag = True
                for k in back[i - foregroundAppList[j][1]]:
                    found.append([j + 1, k])
        if flag:
            break
    return found

print(optimalUtilization(20, [[1, 8], [2, 7], [3, 9], [4, 9]],
                         [[1, 8], [2, 11], [3, 12], [4, 11]]))


