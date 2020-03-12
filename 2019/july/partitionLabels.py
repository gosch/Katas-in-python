class Solution:
    def partitionLabels(self, S):
        dic = {}
        for i, letter in enumerate(S):
            dic[letter] = i

        last_start, cur_last = 0, 0
        result = []
        for i, letter in enumerate(S):
            cur_last = max(cur_last, dic[letter])
            if i == cur_last:
                result.append(i - last_start + 1)
                last_start = i + 1
        return result


in1 = "ababcbacadefegdehijhklij"
obj = Solution()
print(obj.partitionLabels(in1))

