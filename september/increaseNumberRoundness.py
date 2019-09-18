def increaseNumberRoundness(n):
    c = 0
    ns = str(n)
    e = len(ns)
    for i in range(e):
        if ns[i] == '0':
            for j in range(i+1, e):
                if ns[j] != '0':
                    return True
            break
    return False


print(increaseNumberRoundness(902200100))