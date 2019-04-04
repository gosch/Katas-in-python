def reverseInParentheses(inputString):
    s = []
    r = ""
    for c in inputString:
        if c == '(':
            s.append([])
        elif c == ')':
            if len(s) < 2:
                t = s.pop()[::-1]
                r += ''.join(t)
            else:
                s[-2].append(s.pop()[::-1])
        else:
            if len(s) > 0:
                s[-1].append(c)
            else:
                r += c
    return r


print(reverseInParentheses("foo(bar(baz))blim"))
