def reverseParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return reverseParentheses(s[:start] + s[end-1:start:-1] + s[end+1:])
    return s

print(reverseParentheses('a(bc)de'))

