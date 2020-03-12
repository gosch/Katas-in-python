def candles(candlesNumber, makeNew):
    leftover = 0
    total = candlesNumber
    while candlesNumber > 0:
        leftover += candlesNumber
        candlesNumber = leftover // makeNew
        leftover %= makeNew
        total += candlesNumber
    return total


print(candles(5, 2))
