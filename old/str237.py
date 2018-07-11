import time


def calculate(x, p, f, l):
    if f < x[-1]:
        return 0
    c = 0

    for i in range(p, l):
        if x[i] == f:
            c += 1
        if i < l - 1:
            if f - x[i] > 0:
                c += calculate(x, i + 1, f-x[i], l)
    return c


def str237(s):
    s = list(map(lambda x: ord(x), list(s)))
    s = sorted(s, reverse=True)
    return calculate(s, 0, 237, len(s))

before = time.time()
print(str237('The Cameroon country code 237 will allow you to call Cameroon from another country. Cameroon telephone code 237 is dialed after the IDD. Cameroon international dialing 237 is followed by an area code.'))
now = time.time()
print(now - before)
