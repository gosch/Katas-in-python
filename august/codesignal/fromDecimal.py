def fromDecimal(b, n):
    number = []
    counter = 1
    while n > 0:
        tem = n%(b**counter)
        number.append(str(tem))
        n -= tem
    return ''.join(number)


print(fromDecimal(2, 13))
