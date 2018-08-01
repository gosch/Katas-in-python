def countSumOfTwoRepresentations2(n, l, r):
    counter = 0
    for i in range(l, r + 1):
        a = i
        b = n - a
        if b <= r + 1 and b >= a:
            counter += 1
            print(str(a) + ' ' + str(b))

    return counter


def countSumOfTwoRepresentations1(n, l, r):
    counter = 0
    for i in range(l, r + 1):
        a = i
        for j in range(i, r + 1):
            b = j
            if a + b == n:
                counter += 1
                print(str(a) + ' ' + str(b))
    return counter

print(countSumOfTwoRepresentations2(93, 24, 58))
print(countSumOfTwoRepresentations1(93, 24, 58))


