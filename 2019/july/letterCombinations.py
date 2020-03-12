class Solution:

    def letterCombinations(self, digits):
        chars = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        r = self.recursive_combination(digits[:], chars)
        return r

    def recursive_combination(self, digits, chars):

        r = []
        if len(digits) < 1:
            return r
        if len(digits) < 2:
            for i in chars[int(digits[0]) - 2]:
                r.append(i)
            return r
        d = digits[0]
        sub = chars[int(d) - 2]
        sub_result = self.recursive_combination(digits[1:], chars)
        for c in sub:
            for d in sub_result:
                r.append(c + d)
        return r


input1 = "0000"
s = Solution()
print(s.letterCombinations(input1))
