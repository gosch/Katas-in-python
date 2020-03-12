from collections import deque
import heapq


class Solution:
    def cutOffTree(self, forest) -> int:
        # maximum matrix size is 50x50, meaning that at most, trees will be in range [2, 251]
        # but there is no indication that trees are mapped to this range in the input so we'll do it ourselves.
        # afterwards, let int z denote which tree you're looking for, the target.
        # the state for BFS is then uniquely determined by x = row, y = col, z = target
        trees = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], [i, j]))
        heapq.heapify(trees)
        height = 2
        while len(trees) > 0:
            tree = heapq.heappop(trees)
            forest[tree[1][0]][tree[1][1]] = height
            height += 1
        finishHeight = height  # when you've seen all trees you should be looking for a tree of height finishHeight

        q = deque()
        q.appendleft([0, 0, 2])
        visited = set()
        visited.add((0, 0, 2))
        moves = 0

        def neighbors(x, y):
            res = []
            if x - 1 >= 0 and forest[x - 1][y] != 0: res.append([x - 1, y])
            if x + 1 < len(forest) and forest[x + 1][y] != 0: res.append([x + 1, y])
            if y - 1 >= 0 and forest[x][y - 1] != 0: res.append([x, y - 1])
            if y + 1 < len(forest[0]) and forest[x][y + 1] != 0: res.append([x, y + 1])
            return res

        while len(q) > 0:
            n = len(q)
            for i in range(n):
                [x, y, z] = q.popleft()
                if forest[x][y] == z: z += 1
                if z == finishHeight: return moves
                for [x2, y2] in neighbors(x, y):
                    if (x2, y2, z) not in visited:
                        visited.add((x2, y2, z))
                        q.append([x2, y2, z])
            moves += 1
        return -1


inp2 = [[54581641, 64080174, 24346381, 69107959],
        [86374198, 61363882, 68783324, 79706116],
        [668150,   92178815, 89819108, 94701471],
        [83920491, 22724204, 46281641, 47531096],
        [89078499, 18904913, 25462145, 60813308]]
sol1 = Solution()
print(sol1.cutOffTree(inp2))