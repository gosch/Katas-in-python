def caesarBoxCipherEncoding(inputString):
    size = int(len(inputString) ** (0.5))

    message = ['0'] * len(inputString)
    for i in range(size):
        for j in range(size):
            message[j * size + i] = inputString[i * size + j]
    return ''.join(message)

print(caesarBoxCipherEncoding('a message'))
