from itertools import permutations


def neighbors(n, d):
    for cand in permutations(str(n)):
        x = int("".join(cand))
        # yield x
        if x % d:
            continue
        return int(x / d)


def truncateString(s):
    flag = True
    while flag:
        flag = False
        if len(s) == 0:
            return ''
        if int(s[0]) % 3 == 0:
            s = s[1:]
            flag = True
        if int(s[-1]) % 3 == 0:
            s = s[:-1]
            flag = True
        if (int(s[0]) + int(s[-1])) % 3 == 0:
            s = s[1:-1]
            flag = True
    return ''.join(s)


def numberMinimization(n, d):
    n = int(n)
    seen = set()
    stack = [n]
    ct = 0
    while stack:
        ct += 1
        node = stack.pop()
        for nei in neighbors(node, d):
            if nei not in seen:
                seen.add(nei)
                stack.append(nei)
        if ct > 10000:
            return min(seen)
    return min(seen)

# print(numberMinimization(4006, 2))
print(truncateString(312248))
