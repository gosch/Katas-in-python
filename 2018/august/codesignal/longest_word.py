def longestWord(text):
    word = ''
    # temp = text[:]
    # text = text.lower()
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    best_word = ''
    for i in text:
        c = ord(i)
        if a <= c <= z or A <= c <= Z:
            word += i
        else:
            if len(word) == 0:
                continue
            else:
                if len(best_word) < len(word):
                    best_word = word
            word = ''

    return best_word

print(longestWord('ABCd'))
