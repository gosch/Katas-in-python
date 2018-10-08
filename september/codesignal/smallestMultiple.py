

def smallestMultiple(left, right):
    start = min(left, right)
    flag = True
    while flag:
        flag = False
        for i in range(left, right+1):
            if start % i != 0 or start % i != 0:
                flag = True
                break
        if not flag:
            break
        start += 1

    return start


print(smallestMultiple(2, 4))
