def speedingForCandy(streets, n, k):
    ns = len(streets)
    t = [0] * ns
    for i in range(ns):
        size = len(streets[i])
        max_sum = [0 for _ in range(size)]
        max_sum[0] = streets[i][0]
        current = streets[i][0]
        for j in range(1, size):
            current = max(streets[i][j], current + streets[i][j])
            max_sum[j] = current

        k_elements_sum = sum(streets[i][:n])
        max_total = k_elements_sum
        for j in range(n, size):
            k_elements_sum += streets[i][j] - streets[i][j-n]
            max_total = max(max_total, k_elements_sum)
            max_total = max(max_total, k_elements_sum + max_sum[j-n])

        t[i] = max_total
    t = sorted(t, reverse=True)
    r = 0
    for i in range(k):
        if t[i] < 0:
            break
        else:
            r += t[i]
    return r

def speedingForCandy(streets, n, k):
    ns = len(streets)
    t = [0] * ns
    for i in range(ns):
        size = len(streets[i])
        max_sum = [0 for _ in range(size)]
        max_sum[0] = streets[i][0]
        current = streets[i][0]
        for j in range(1, size):
            current = max(streets[i][j], current + streets[i][j])
            max_sum[j] = current

        k_elements_sum = sum(streets[i][:n])
        max_total = k_elements_sum
        for j in range(n, size):
            k_elements_sum += streets[i][j] - streets[i][j-n]
            max_total = max(max_total, k_elements_sum)
            max_total = max(max_total, k_elements_sum + max_sum[j-n])

        t[i] = max_total
    t = sorted(t, reverse=True)
    r = 0
    for i in range(k):
        if t[i] < 0:
            break
        else:
            r += t[i]
    return r

streets = [ [4,-2,6,4,6], [3,7,-4,-4,1],
 [-1,2,2,1,1]
]
n = 3
k = 2
print(speedingForCandy(streets, n, k))

