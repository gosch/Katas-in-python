def createAnagram(s, t):
    s = sorted(s)
    t = sorted(t)

    counter = 0
    temp1 = [0] * 26
    for i in range(len(s)):
        temp1[ord(s[i]) - ord('A')] += 1
        temp1[ord(t[i]) - ord('A')] -= 1

    for i in range(26):
        if temp1[i] != 0:
            counter += 1
    return counter/2

def sumOfMultiples(n, k):
    counter = 0
    for i in range(k, n+1, k):
        counter += i
    return i





def maximumSubsetProduct(a):
    n = 0 - int(float('inf'))
    c = 0
    for i in a:
        if i < 1:
            n = i
            c += 1
    if c % 2 == 0:
        return 1
    else:
        return n


# print(createAnagram('AABAA', 'BBAAA'))
print(sumOfMultiples(7, 2))
