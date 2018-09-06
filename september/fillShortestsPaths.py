max_counter = 9999999


def find_plan(step):
    pass



def fillShortestPaths(plan):
    plans = {}
    grid = [0] * len(plan[0]) * len(plan)


    for i in range(len(plan)):
        for j in range(len(plan[i])):
            if plan[i][j] == 's':
                grid[i][j] = 1
                if i == 0 or j == 0:
                    return 1
                else:
                    steps, plan = find_plan(1)
                    plans[steps].append(plan)









