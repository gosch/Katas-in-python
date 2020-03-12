class Solution:
    def longestPalindrome(self, s: str) -> str:

        for i in range(len(s)):
            j = 0
            s1 = (len(s) - i) // 2
            while j < len(s) - (len(s) - i) + 1:
                s2 = s1 + j if s1 * 2 == len(s)-i else s1 + j + 1
                if s[j:j+s1] == s[s2:s2+s1][::-1]:
                    return s[j:s2+s1]
                j += 1
        return ""


obj = Solution()
print(obj.longestPalindrome("babad"))
