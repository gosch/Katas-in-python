import math


class Solution:
    def kClosest(self, points, K):
        distances = [{"pos": i, "dis": math.sqrt(val[0] ** 2 + val[1] ** 2)} for i, val in enumerate(points)]
        return [points[e["pos"]][::] for e in sorted(distances, key=lambda k: k["dis"])][:K]

    def kClosest2(self, points, K):
        points = sorted(points, key=lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2))


obj = Solution()
print(obj.kClosest([[1, 3], [-2, 2]], 1))





