def str237(str):
    values = []
    target = 237

    for c in str:
        values.append(ord(c))

    array = [1] + [0] * target
    values.sort(reverse=True)

    for current_number in values:
        for possible_num in range(target, current_number - 1, -1):
            pos = possible_num - current_number
            if array[pos] == 1:
                array[possible_num] += array[pos]

    return array[target]

print(str237("Heo Wrld"))