class Solution:
    def prisonAfterNDays(self, cells, N: int):

        newTemp = [0] * 6

        mem = {}

        # first day
        a = 0
        c = 0
        count = -1

        for j in range(1, 7):
            newTemp[j-1] = 1 if cells[j - 1] == cells[j + 1] else 0
        # mem[tuple(cells[1:7])] = tuple(newTemp)
        temp = tuple(newTemp)
        sol_list = []
        if N == 1:
            return [0] + list(temp) + [0]
        print("D0" + str(cells))
        # print("D1" + str([0] + list(temp) + [0]))
        for i in range(N):
            if temp in mem:

                for j, sol in enumerate(sol_list):
                    if temp == sol:
                        c = j
                        count = len(sol_list) - j
                        break
                break

            else:
                for j in range(6):
                    if j == 0:
                        newTemp[j] = 1 if 0 == temp[j + 1] else 0
                    elif j == 5:
                        newTemp[j] = 1 if 0 == temp[j - 1] else 0
                    else:
                        newTemp[j] = 1 if temp[j - 1] == temp[j + 1] else 0
                mem[temp] = tuple(newTemp)
                sol_list.append(temp)
                print(str(i+1) + " " + str([0] + list(temp) + [0]))
                temp = tuple(newTemp)

                a += 1

        N -= a + 1
        b = N % count if count != -1 else len(sol_list) - 1
        # b = b - 1 if b - 1 >= 0 else len(sol_list) - 1
        return [0] + list(sol_list[c + b]) + [0]


# inp = [1, 1, 0, 1, 1, 0, 0, 0]
# n = 1

# inp = [1, 0, 0, 1, 0, 0, 1, 0]
# n = 1000000000
inp = [0, 1, 0, 1, 1, 0, 0, 1]
n = 7
obj = Solution()
print(" f " + str(obj.prisonAfterNDays(inp, n)))
