
def rounders(n):
    # l = (len(str(n)) - 1)
    # n /= 10**l
    # return int(round(n) * 10**l)
    s = list(str(n))
    i = len(s) - 1
    carry = 0
    while i > 0:
        if int(s[i]) + carry >= 5:
            s[i] = 0
            carry = 1
        i -= 1

    if s[0] + carry
    s[i] = '0'
    return int(''.join(s))

print(rounders(15))
