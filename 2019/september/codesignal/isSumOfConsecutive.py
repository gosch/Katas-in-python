def isSumOfConsecutive(n):
    if n < 2:
        return False
    divisor = 2
    dif = 1
    counter = 1
    while divisor < n:
        if (n - dif) % divisor == 0:
            return True
        counter += 1
        dif += counter
        divisor += 1

    return False


print(isSumOfConsecutive(1000_000_000_000_000))
