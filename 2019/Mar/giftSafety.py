import itertools


def giftSafety(gift):
    r = 0
    for i in range(0, len(gift) - 2):
        c = 0
        c_per = gift[i:i + 3]
        for per in itertools.permutations(c_per):
            if ''.join(per) == c_per:
                c += 1
            if c == 2:
                r += 1
                break
    return r


print(giftSafety("doll"))
