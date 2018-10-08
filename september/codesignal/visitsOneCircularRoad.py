def visitsOnCircularRoad(n, visitsOrder):
    r = 0
    visitsOrder = [1] + visitsOrder
    for i in range(len(visitsOrder) - 1):
        r += abs(visitsOrder[i] - visitsOrder[i + 1]) if abs(visitsOrder[i] - visitsOrder[i + 1]) <= n / 2 else abs(visitsOrder[i] - visitsOrder[i + 1]) // 2
    return r


print(visitsOnCircularRoad(4, [1, 3, 2, 3, 1]))
