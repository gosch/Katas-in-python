def minimumOnStack(operations):
    r = []
    values = []
    for i in operations:
        a = i.split(" ")
        if a[0] == "push":
            values.append(int(a[1]))
        elif a[0] == "pop":
            del(values[-1])
        else:
            r.append(min(values))
    return r


