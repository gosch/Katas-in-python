class Solution:
    def reverse(self, x: 'int') -> 'int':

        value = int(str(abs(x))[::-1])
        value = value if x >= 0 else -value
        if value >= 0x80000000 or value < -0x80000000:
            return 0
        else:
            return value


s = Solution()
print(s.reverse(123))
