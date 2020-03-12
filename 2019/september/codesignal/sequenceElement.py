def sequenceElement(a, n):
    seq = a[:]
    i = 5
    last = a[0] * 1e4 + a[1] * 1e3 + a[2] * 1e2 + a[3] * 10 + a[4]
    seq_dic = {}
    while True:
        seq.append(sum(seq[i - 5:i]) % 10)
        last = (last * 10 + seq[i]) % 1e5
        if last in seq_dic:
            l = seq_dic[last]
            return seq[n % (i - l)]
        else:
            seq_dic[last] = i
        i += 1

    return -1


print(sequenceElement([1, 2, 3, 4, 5], 9))
