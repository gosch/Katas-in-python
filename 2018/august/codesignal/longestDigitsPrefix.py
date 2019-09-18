def longestDigitsPrefix(inp):
    num = ''
    biggest = ''
    flag = False
    for i in range(len(inp)):
        if inp[i].isdigit():
            if flag:
                num += str(inp[i])
            else:
                flag = True
                num = str(inp[i])
        else:
            flag = False
            num = ''

        if len(num) > len(biggest):
            biggest = num
    return biggest


# print(longestDigitsPrefix('inputString: "  3) always check for whitespaces"'))
print(longestDigitsPrefix('the output is 42'))