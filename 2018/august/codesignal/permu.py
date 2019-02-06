from itertools import permutations


def fibonacciSum(n):
    fib = [0, 1]
    curr = 0
    while curr <= n:
        curr = fib[-1] + fib[-2]
        fib.append(curr)


    fib = fib[::-1]
    curr = 0
    r = []
    while n > 0:
        if n - fib[curr] >= 0:
            n-= fib[curr]
            r.append(fib[curr])
        curr+=1
    return r[::-1]




print(fibonacciSum(33))