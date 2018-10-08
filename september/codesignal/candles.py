def candles(candlesNumber, makeNew):
    total = candlesNumber
    portions = 0
    while candlesNumber >= 1:
        new_candles = candlesNumber // makeNew
        portions += candlesNumber % makeNew / makeNew
        if portions >= 1:
            portions -= 1
            new_candles += 1
        candlesNumber = new_candles
        total += new_candles
    return total

print(candles(5, 2))
