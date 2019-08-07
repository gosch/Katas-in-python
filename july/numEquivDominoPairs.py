import math

class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        acu = 0
        mem = {}
        for i in dominoes:
            if (i[0], i[1]) in mem:
                mem[i[0], i[1]] += 1
                mem[i[1], i[0]] += 1 if i[0] != i[1] else 0
            else:
                mem[i[0], i[1]] = 1
                mem[i[1], i[0]] = 1
        for i in mem.keys():
            if mem[i[0], i[1]] > 1:
                acu += math.factorial(mem[i[0], i[1]]) // (2 * math.factorial(mem[i[0], i[1]] - 2))
                mem[i[0], i[1]] = 1
                mem[i[1], i[0]] = 1

        return acu


in1 = [[2, 1], [1, 2], [1, 2], [1, 2], [2, 1], [1, 1], [1, 2], [2, 2]]
s = Solution()
print(s.numEquivDominoPairs(in1))
