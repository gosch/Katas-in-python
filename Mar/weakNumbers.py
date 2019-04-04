def weakNumbers(n):
    divisors = []
    for i in range(1, n + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        divisors.append(count)

    weakness = []
    for i in range(len(divisors)):
        count = 0
        for j in range(0, i):
            if divisors[j] > divisors[i]:
                count += 1
        weakness.append(count)

    weakness.sort(reverse=True)
    count = 1
    for i in range(1, len(weakness)):
        if weakness[i] == weakness[0]:
            count += 1
        else:
            break

    return [weakness[0], count]


print(weakNumbers(9))
