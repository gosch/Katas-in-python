def symbolsPermutation(word1, word2):

    if len(word1) != len(word2):
        return False
    char_a = [0] * 26
    a = ord('a')
    for i in range(len(word1)):
        char_a[ord(word1[i]) - a] += 1
        char_a[ord(word2[i]) - a] -= 1

    for i in range(26):
        if char_a[i] != 0:
            return False
    return True


print(symbolsPermutation('abc', 'cab'))
