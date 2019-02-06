def factorSum(n):
    primes = []
    flag = True

    import math
    for i in range(2, 99):
        is_prime = True
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                is_prime = False
        if is_prime:
            primes.append(i)

    while flag:
        i = 0
        if n in primes:
            return n
        factors_found = []
        before = n
        while i < 7:
            if n % primes[i] == 0:
                n = n / primes[i]
                flag = True
                factors_found.append(primes[i])
                i = 0
            else:
                i += 1
        temp = 0

        for i in factors_found:
            temp += i
        if temp == 0:
            flag = False
        if temp == before:
            return before
        n = temp

    return n


print(factorSum(24))
