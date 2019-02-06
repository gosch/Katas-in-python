def roverTour(terrain_difficulty: list, energy):
    longest_path = 0
    for i in range(len(terrain_difficulty)):
        current_path = 1
        sum1 = terrain_difficulty[i]
        for j in range(i + 1, len(terrain_difficulty)):
            if terrain_difficulty[j] + sum1 <= energy:
                sum1 += terrain_difficulty[j]
                current_path += 1
            else:
                break
        longest_path = current_path if longest_path < current_path else longest_path
    return longest_path


def roverTour2(terrain_difficulty: list, energy):
    longest_path = 1
    n = len(terrain_difficulty)
    memory_path_count = [0] * n
    memory = [1] * n
    memory[0] = terrain_difficulty[n - 1]
    pointer = 1
    counter = 0
    memory_path_count[0] = 1
    for i in range(n - 2, -1, -1):
        j = 0
        deleted_solutions = 0
        while j < pointer - deleted_solutions:
            if terrain_difficulty[i] + memory[j] <= energy:
                memory[j] += terrain_difficulty[i]
                memory_path_count[j] += 1
                j += 1
            else:
                del memory[j]
                longest_path = memory_path_count[j] if longest_path < memory_path_count[j] else longest_path
                del memory_path_count[j]
                deleted_solutions += 1
        pointer += 1 - deleted_solutions
        counter += 1
        memory[pointer - 1] = terrain_difficulty[i]
        memory_path_count[pointer - 1] = 1
    mem_max = max(memory_path_count)
    longest_path = mem_max if longest_path < mem_max else longest_path
    return longest_path

def roverTour3(t, e):

    a = 0
    p = 0
    c = 0
    s = 0
    for i in t:
        while i + a > e:
            a -= t[p]
            p += 1
            c -= 1
        a += i
        c += 1
        s = c if s < c else s
    return s


terrainDifficulty1 = [1, 3, 2, 5, 4, 7, 3, 5, 6, 2, 8, 81, 3, 5, 2, 4, 5, 1, 6, 3, 4, 7, 2, 5]
energy1 = 100

print(roverTour3(terrainDifficulty1, energy1))
