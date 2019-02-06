def dashes(n):
    string = "-"
    length = n * 2 - 10
    for i in range(n):
        for j in range(i):
            str += '-'
        str += '|'
    return string
