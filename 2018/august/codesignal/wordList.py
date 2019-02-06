def unusualDictionary(wordList):
    ordered_words = sorted(wordList, key=lambda word: (word.split(" ")[1] if len(
        word.split(" ")) > 1 else word, word.split(" ")[0]))

    for i, w in enumerate(wordList):
        if w != ordered_words[i]:
            return False
    return True


wordList = ["the cat",
 "to hiss",
 "a kitten",
 "to meow",
 "playful",
 "to purr"]

wordList2 = ["to desert", "the desert", "a dessert"]
wordList3 = ["a",
             "an a",
             "to a",
             "a b",
             "b",
             "to b"]

# word_test = wordList[0].split(" ")
# print(unusualDictionary(wordList))
# print(unusualDictionary(wordList2))
print(unusualDictionary(wordList3))
