def properOrImproper(a):
    return 'Proper' if abs(a[0] / (a[1] * 1.0)) < 1 else 'Improper'

def depositProfit(deposit, rate, t):
    y = 0
    while deposit < t:
        deposit *= (1+rate/100.0)


print(properOrImproper([2, 3]))
