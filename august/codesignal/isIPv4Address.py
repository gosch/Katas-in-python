def isIPv4Address(inputString):
    r = inputString.split('.')
    if len(r) != 4:
        return False
    for i in r:
        if not i.isdigit():
            return False
        v = int(i)
        if v < 0 or v > 255:
            return False
    return True

print(isIPv4Address('172.16.254.1'))
