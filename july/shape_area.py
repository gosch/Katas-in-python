
def calculate_diag(n, memory):

    memory = [0]
    for ind in range(1, n):
        memory.append(ind + memory[ind - 1])

    return memory[n-1]

def shape_area(n):
    memory = None
    diag = calculate_diag(n, memory)
    return (n*2 - 1) ** 2 - diag * 4

def shape_area2(n):
    return n**2 + (n-1)**2


if __name__ == '__main__':
    # print(shape_area(1))
    # print(shape_area(2))
    for i in range(1, 992):
        case1 = shape_area(i)
        case2 = shape_area2(i)
        if case1 != case2:
            print('Case ' + str(i) + ' == ' + str(case1) + ' != ' + str(case2))
    print()

