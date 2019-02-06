class Solution:
    def twoSum(self, nums, target):
        """
        :param nums:
        :param target:
        :return:
        """
        map_values = {}
        for index, item in enumerate(nums):
            difference = target - item
            if difference not in map_values:
                map_values[item] = index
            else:
                return [map_values[difference], index]

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
