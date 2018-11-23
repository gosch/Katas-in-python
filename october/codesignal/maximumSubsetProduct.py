def maximumSubsetProduct(a):
    count_0 = 0
    min_0 = -9999999999
    if len(a) == 1 and a[0] < 0:
        return 1

    for i in a:
        if i < 0:
            count_0 += 1
            if min_0 < i:
                min_0 = i

    if count_0 % 2 == 1:
        return min_0
    else:
        return 1


# print(maximumSubsetProduct([1, 2, -2, -3, 3, 5]))
a = [1, 2, -2, -3, 3, 5]

val = list(i < 0 for i in a)
print(sum(val))