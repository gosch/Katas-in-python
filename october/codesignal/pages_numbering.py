import math

def pagesNumbering(n):
    ln_n = math.log10(n) + 1
    r = int(ln_n) * n

    c = 1
    while c < int(ln_n):
        r -= 10**c - 1
        c+=1

    return r


print(pagesNumbering(1000))
