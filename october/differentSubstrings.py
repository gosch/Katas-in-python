def differentSubstrings(inputString):
    sub_strings = set()

    for i in range(1, len(inputString) + 1):
        for j in range(len(inputString)):
            sub_strings.add(inputString[j:j+i])
    return len(sub_strings)

print(differentSubstrings("abac"))

