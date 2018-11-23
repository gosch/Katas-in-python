def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    elif weight1 <= maxW:
        if weight2 <= maxW:
            if value1 > value2:
                return value1
            else:
                return value2
        else:
            return value1

    elif weight2 <= maxW:
        return value2
    return 0



