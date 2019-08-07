import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:

        regex = re.compile('[^a-z ]')

        words = regex.sub('', paragraph.lower()).split()

        count = {}

        for word in words:
            if word not in banned:
                if word not in count:
                    count[word] = 1
                else:
                    count[word] += 1
        max_word = ""
        max_count = 0
        for k, v in count.items():
            if v > max_count:
                max_word = k
                max_count = v

        return max_word


sol = Solution()
print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
