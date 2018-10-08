

def digitalSumSort(a):
    return sorted(a, key=lambda v: sum([int(i) for i in str(v)]))

print(digitalSumSort([12, 4, 1]))