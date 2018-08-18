def longestDigitsPrefix(inputString):
    num = ''
    biggest = ''
    flag = False
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            if flag:
                num += str(inputString[i])
            else:
                flag = True
                num = str(inputString[i])
        else:
            flag = False
            num = ''

        if len(num) > len(biggest):
            biggest = num
    return biggest


# print(longestDigitsPrefix('inputString: "  3) always check for whitespaces"'))
print(longestDigitsPrefix('the output is 42'))