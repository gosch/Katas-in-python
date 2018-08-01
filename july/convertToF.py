def convertToF(temp):
    return 9 * temp / 5 + 32


def celsiusVsFahrenheit(yourTemps, friendsTemps):
    counter = 0
    for i in range(len(friendsTemps)):
        if convertToF(yourTemps[i]) <= friendsTemps[i]:
            counter += 1
    return counter

print(celsiusVsFahrenheit([26], [77]))