from itertools import combinations


def countWays2(n, k):
    p = q = 1
    while k:
        q *= k
        k -= 1
        p *= n - k

    return p // q % (10 ** 9 + 7)

def countWays(n, k):
    return len(list(combinations(range(n), k))) % (10 ** 9 + 7)


print(countWays(5, 2))