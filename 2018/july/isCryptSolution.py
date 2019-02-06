def isCryptSolution(crypt, solution):
    let_dic = []
    code = [-1 for i in range(26)]
    for c in solution:
        code[ord(c[0]) - ord('A')] = int(c[1])
        if c[1] is '0':
            let_dic.append(c[0])

    for i, word in enumerate(crypt):
        if len(word) > 1:
            if word[0] in let_dic:
                return False

    word1 = ''.join([str(code[ord(j) - ord('A')]) for j in crypt[0]])
    word2 = ''.join([str(code[ord(j) - ord('A')]) for j in crypt[1]])
    word3 = ''.join([str(code[ord(j) - ord('A')]) for j in crypt[2]])
    return int(word1) + int(word2) == int(word3)

crypt_in = ["A",
            "B",
            "C"]
solution= [["A", "5"],
           ["B", "6"],
           ["C", "1"]]
print(isCryptSolution(crypt_in, solution))
