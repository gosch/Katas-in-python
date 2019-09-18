def squareDigitsSequence(a0):
    values = [i ** 2 for i in range(10)]
    num_seq = set()
    n = a0
    while not n in num_seq:
        val = 0
        num_seq.add(n)
        while n > 0:
            val += values[n % 10]
            n //= 10
        n = val
    return len(num_seq) + 1


print(squareDigitsSequence(16))
