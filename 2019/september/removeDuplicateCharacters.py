def removeDuplicateCharacters(st):
    for i in range(len(st) - 1):
        if st[i] in st[i + 1:]:
            st = st.replace(st[i], ' ')
    return st.replace(' ', '')


print(removeDuplicateCharacters("zaabcbd"))
