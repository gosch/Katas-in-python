class Solution:
    def twoSum(self, numbers, target):
        """
        :param numbers:
        :param target:
        :return:
        """
        map_values = {}
        for index, item in enumerate(numbers):
            difference = target - item
            if difference not in map_values:
                map_values[item] = index
            else:
                return [map_values[difference] + 1, index + 1]


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
