def firstDuplicate(a):
    dic = {}
    for i in range(len(a)):
        if a[i] in dic:
            return a[i]
        else:
            dic[a[i]] = i
    return -1

print(firstDuplicate([2, 4, 3, 5, 1]))
