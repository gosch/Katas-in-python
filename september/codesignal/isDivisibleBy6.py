# A masked number is a string that consists of digits and one asterisk (*) that should be replaced by exactly one
# digit. Given a masked number find all the possible options to replace the asterisk with a digit to produce an
# integer divisible by 6.
#
# Example
#
# For inputString = "1*0", the output should be
# isDivisibleBy6(inputString) = ["120", "150", "180"].


def isDivisibleBy6(inputString):
    x = inputString.find('*')
    pre = inputString[:x]
    post = inputString[x+1:]
    r = []
    for i in range(10):
        n = ''.join(pre) + str(i) + ''.join(post)
        if int(n) % 6 == 0:
            r.append(n)
    return r


print(isDivisibleBy6('100*0'))
