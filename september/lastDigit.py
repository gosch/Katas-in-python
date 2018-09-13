import timeit

def lastDigit(a, b):
    return a**b%10


print(timeit.timeit(setup='', stmt='999999**1000000%10'))
