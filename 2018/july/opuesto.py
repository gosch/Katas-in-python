def reflectString(inputString):
    result = []
    for i in inputString:
        result.append(chr(ord('z') + (ord('a') - ord(i))))
    return ''.join(result)


print(reflectString('name'))