
class Solution:

    def isRectangleOverlap(self, rec1, rec2):

        top_left = (rec1[0], rec1[3])
        bottom_right = (rec1[2], rec1[1])
        top_left2 = (rec2[0], rec2[3])
        bottom_right2 = (rec2[2], rec2[1])

        if top_left[0] > bottom_right2[0] or top_left2[0] > bottom_right[0]:
            return False
        if top_left[1] > bottom_right2[1] or top_left2[1] > bottom_right[1]:
            return False
        return True


sol = Solution()
print(str(sol.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3])))
