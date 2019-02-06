def areSimilar(a, b):
    flag = False
    flag2 = False
    for i in range(len(a)):
        if a[i] != b[i]:
            if flag:
                if flag2:
                    return False
                if a[i] != b1 or b[i] != a1:
                    return False
                else:
                    flag2 = True
            else:
                a1 = a[i]
                b1 = b[i]
                flag = True
    return True


print(areSimilar([1, 2, 3], [1, 10, 2]))
