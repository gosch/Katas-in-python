class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        st1 = len(str1)
        st2 = len(str2)
        temp = str2[:st2]
        divisor = 1
        while str1 != (temp * (st1 // len(temp))) or str2 != (temp * (st2 // len(temp))):
            divisor += 1
            if st2 // divisor == 0:
                temp = ""
                break
            temp = str2[:st2 // divisor]

        return temp


s1 = "ABCABC"
s2 = "ABC"

s1 = "ABABAB"
s2 = "ABAB"
s = Solution()
print(s.gcdOfStrings(s1, s2))
