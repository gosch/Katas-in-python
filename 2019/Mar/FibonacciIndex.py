import math

def fibonacciIndex(n):

    f1 = 0
    f2 = 1
    c = 1
    k = 2
    if n == 1:
        return 0
    while int(math.log(c, 10)) + 1 < n:
        c = f1 + f2
        f1 = f2
        
        f2 = c
        k += 1
    return k - 1


print(fibonacciIndex(2))
