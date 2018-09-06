def lazyFriends(houses, maxDist):
    res = [0] * len(houses)
    l = r = 0
    for i in range(len(houses)):

        j = l
        while j < len(houses):
            if houses[i] - houses[j] > maxDist:
                j += 1
                l = j
            else:
                break
        j = r
        while j < len(houses):
            if houses[j] - houses[i] <= maxDist:
                r = j
            else:
                break
            j += 1

        res[i] = r - l
    return res


print(lazyFriends([-5, 0, 5, 10, 15], 10))
