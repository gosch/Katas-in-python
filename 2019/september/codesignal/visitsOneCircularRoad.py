def visitsOnCircularRoad(n, visitsOrder):
    r = 0
    visitsOrder = [1] + visitsOrder
    for i in range(len(visitsOrder) - 1):
        mx = max(visitsOrder[i+1], visitsOrder[i])
        mn = min(visitsOrder[i+1], visitsOrder[i])
        r += min(mx - mn, (mn + n) - mx)
    return r


print(visitsOnCircularRoad(4, [1, 3, 2, 3, 1]))
