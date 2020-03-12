def bs(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2;
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1

def maxPairProduct(a):
    a = sorted(a, reverse=True)
    r = -1
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] % a[j] != 0:
                continue
            v = a[i] / a[j]
            if v > a[j]:
                r = bs(a, 0, j - 1, v)
            else:
                r = bs(a, j + 1, len(a) - 1, v)

            if r != -1:
                return a[i]
    return r


a = [10, 3, 5, 30, 35]
print(maxPairProduct(a))
