import copy


def calculateNeighbors(start, des):
    x1 = start[0]
    y1 = start[1]
    x2 = des[0]
    y2 = des[1]
    distances = list()
    distances.append(((x1 + 1, y1),  abs(x2 - (x1+1)) + abs(y2 - y1)))
    distances.append(((x1,  y1 + 1), abs(x2 - x1) + abs(y2 - y1)))
    distances.append(((x1 - 1, y1), abs(x2 - (x1 - 1)) + abs(y2 - y1)))
    distances.append(((x1, y1 - 1), abs(x2 - x1) + abs(y2 - (y1 - 1))))
    distances = sorted(distances, key=lambda k: k[1])
    neighbors = [i[0] for i in distances]
    return neighbors


class Solution:

    def cutOffTree(self, forest) -> int:
        trees = []

        for i in range(len(forest)):
            for j in range(len(forest[i])):
                tree = forest[i][j]
                if tree > 1:
                    trees.append({'tall': tree, 'pos': (i, j)})
        trees = sorted(trees, key=lambda k: k['tall'])
        c_pos = (0, 0)
        steps = 0
        i = 1
        configu = [[0 for _ in range(len(forest[0]))] for _ in range(len(forest))]

        for tree in trees:
            configu[tree['pos'][0]][tree['pos'][1]] = i
            i += 1
        self.print_solution(configu)

        for tree in trees:
            maze = copy.deepcopy(forest)
            mem = {}
            step = self.solve_maze(maze, (len(forest), len(forest[0])), c_pos, tree['pos'], mem)
            if step == -1:
                return -1
            steps += step
            c_pos = tree['pos']

        return steps

    @staticmethod
    def is_safe(maze, x, y, size):
        if size[0] > x >= 0 <= y < size[1] and 0 != maze[x][y]:
            return True
        return False

    def solve_maze(self, maze, size, start, dest, mem):
        steps = self.solveMazeUtil(copy.deepcopy(maze), start[0], start[1], size, dest, 0, mem)
        return steps

    @staticmethod
    def print_solution(sol):
        for i in sol:
            for j in i:
                print(str(j) + ", ", end="")
            print("")
        print("")

    # A recursive utility function to solve Maze problem
    def solveMazeUtil(self, maze, x, y, size, des, steps, mem):

        # if (x, y is goal) return True

        if x == des[0] and y == des[1]:
            return 0

        # Check if maze[x][y] is valid
        if self.is_safe(maze, x, y, size):

            if (x, y) in mem:
                # return mem[(x, y)]
                return mem[(x, y)]
            else:
                maze[x][y] = 0

                neighbors = calculateNeighbors((x, y), des)

                best_step = -1
                for neighbor in neighbors:
                    steps_temp = self.solveMazeUtil(copy.deepcopy(maze), neighbor[0], neighbor[1], size, des, steps + 1, mem)
                    if best_step == -1:
                        best_step = steps_temp
                    best_step = min(best_step, steps_temp) if steps_temp != -1 else best_step
                    if best_step != 1 and best_step < 3:
                        break

                best_step = best_step + 1
                if best_step != -1:
                    mem[(x, y)] = best_step
                return best_step if best_step != -1 else -1
        return -1


inp1 = [
    [1, 2, 3],
    [0, 0, 4],
    [7, 6, 5]
]

inp2 = [[
          9, 12,  5, 14],
        [17, 11, 13, 15],
        [ 2, 0, 19, 21],
        [16,  4,  7,  8],
        [18,  3,  6, 10]]

inp4 = [[63750247, 40643210, 95516857, 89928134, 66334829, 58741187, 76532780, 45104329],
        [3219401, 97566322, 9135413, 75944198, 93735601, 33923288, 50116695, 83660397],
        [64460750, 53045740, 31903386, 78155821, 90848739, 38769489, 99349027, 85982891],
        [30628785, 51077683, 70534803, 67460877, 91077770, 74197235, 5696362, 91459886],
        [56105195, 82479378, 45937951, 52817583, 2768114, 43329099, 28189138, 21418604]]

inp5 = [[4557, 6199, 7461, 2554, 6132, 7471, 7103, 4290],
        [2034, 2301, 6733, 6040, 2603, 5697, 9541, 6678],
        [7308, 7368, 9618, 4386, 6944, 3923, 4754, 4294],
        [0, 3016, 7242, 5284, 6631, 1897, 1767, 7603],
        [2228, 0, 3625, 7713, 2956, 3264, 3371, 6124],
        [9195, 7804, 2787, 0, 4919, 9304, 5161, 502]]

inp6 = [[2, 3, 4], [0, 0, 5], [8, 7, 6]]
sol1 = Solution()
print(sol1.cutOffTree(inp2))
