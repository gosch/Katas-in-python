def increasingNumber(x, n):

    for i in range(1, n+1):
        while x % i != 0:
            x += 1
    return x


print(increasingNumber(9, 5))
