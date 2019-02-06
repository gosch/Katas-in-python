def competitiveEating(t, width, precision):
    return str("%.{}f".format(precision) % t)


print(competitiveEating(3.1415, 10, 2))
