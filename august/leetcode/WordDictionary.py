class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = dict()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if len(word) in self.items:
            self.items[len(word)].append(word)
        else:
            self.items[len(word)] = [word]

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not self.items or not word:
            return False
        if len(word) not in self.items:
            return False
        if "." not in word:
            return word in self.items[len(word)]

        reduced_list = self.items(len(word))
        if not reduced_list:
            return False
        for w in reduced_list:
            count = 0
            for i in range(len(word)):
                if word[i] == '.' or word[i] == w[i]:
                    count += 1
                if count == len(word):
                    return True
        return False


dic = WordDictionary()
dic.addWord('bad')
dic.addWord('dad')
dic.addWord('mad')
print(dic.search('pad'))
print(dic.search('bad'))
print(dic.search('.ad'))
print(dic.search('b..'))
