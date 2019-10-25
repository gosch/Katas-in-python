def sumOfDivisors(n):
    return sum([0 if n % i != 0 else i if n // i == i else i + n // i for i in range(1, int(n**0.5) +1)])


print(sumOfDivisors(12))
