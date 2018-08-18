def combinationCount2(array1, array2, array3):
    array1.sort()
    array2.sort()
    array3.sort()
    counter = 0
    s1 = len(array1)
    s2 = len(array2)
    s3 = len(array3)
    i1 = i2 = i3 = 0
    for i in range(s2):
        if array2[i] > array1[0]:
            i2 = i
            break
    for i in range(s3):
        if array3[i] > array2[i2]:
            i3 = i
            break
    i = i1
    while i < s1:
        j = i2
        while j < s2:
            k = i3
            while k < s3:
                if array1[i] < array2[j] < array3[k]:
                    counter += s3 - k
                    break
                k += 1
            j += 1
        print(str(counter))
        i += 1

    return counter


def combinationCount(a, a2, a3):
    a.sort()
    a2.sort()
    a3.sort()
    c = 0
    l = len(a)
    i1 = i2 = i3 = 0
    for i in range(l):
        if a2[i] > a[0]:
            i2 = i
            break
    for i in range(l):
        if a3[i] > a2[i2]:
            i3 = i
            break
    i = i1
    while i < l:
        if a[i] >= a2[-1]:
            break
        while a[i] >= a2[i2]:
            i2 += 1
        j = i2
        k = i3
        while j < l:
            if a2[j] >= a3[-1]:
                break
            while a2[j] >= a3[k]:
                k += 1
            c += l - k
            j += 1
        i += 1
    return c

aa1 = [66, 38, 49, 75, 30, 16, 95, 66, 75, 6, 7, 18, 75, 61, 71, 77, 36, 78, 84, 20, 60]
aa2 = [87, 34, 88, 16, 43, 26, 77, 19, 51, 61, 74, 1, 5, 13, 85, 87, 43, 20, 4, 71, 64]
aa3 = [41, 96, 35, 73, 48, 67, 0, 4, 98, 89, 48, 61, 52, 33, 85, 77, 55, 39, 10, 10, 5]
print(combinationCount2(aa1, aa2, aa3))
print('\n')
print(combinationCount(aa1, aa2, aa3))
