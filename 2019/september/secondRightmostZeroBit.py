def secondRightmostZeroBit(n):
    # str(bin(n))[3 + str(bin(n))[2:].index('0'):].index('0') +
    print(bin(n))
    pos = (~ n & ((~n) - 1)) ^ ((~ n & ((~n) - 1)) & ((~ n & ((~n) - 1)) - 1))
    return pos

n = 6
print(n & -n)
