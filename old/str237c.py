def str237(str):
    arr = [ord(x) for x in str]
    memo = dict()
    return rec(arr, 237, len(arr)-1, memo)


def rec(arr, total, i, memo):
    key = str(i)+':'+str(total)
    print(key)
    if key in memo:
        return memo[key]
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        temp = rec(arr, total, i-1, memo)
    else:
        temp = rec(arr, total-arr[i], i-1, memo) + rec(arr, total, i-1, memo)
    memo[key] = temp
    return temp

print(str237('Hello World!!'))
