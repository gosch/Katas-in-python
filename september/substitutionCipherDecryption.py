def substitutionCipherDecryption(contents, signature, encryptedSignature):
    letters_selected = {}
    letter_ord = [-1] * 26

    for i, c in enumerate(encryptedSignature):
        letter_ord[ord(signature[i]) - ord('a')] = ord(c) - ord('a')
        letters_selected[c] = signature[i]

    pos = 0
    for i in range(26):
        c = chr(ord('a') + i)
        if c not in letters_selected:
            while letter_ord[pos] != -1:
                pos += 1
            letter_ord[pos] = ord(c) - ord('a')
            letters_selected[c] = chr(ord('a') + pos)

    message = []
    for i in contents:
        message.append(letters_selected[i])

    return ''.join(message)


print(substitutionCipherDecryption("issomtoqmvjts", "alice", "james"))
