def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def maxZeros(n):
    base = 2

    count = 0
    m_count = 0
    m_base = 2
    for i in range(30):
        base = i + 2
        # str_n = str(int(str(n), base))
        str_n = numberToBase(n, base)
        count = 0
        for s in str_n:
            if s == 0:
                count += 1
        if m_count < count:
            m_count = count
            m_base = base

    return m_base


print(maxZeros(7))
