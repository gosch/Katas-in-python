def numbersGrouping(a):
    base = 10000
    pointers = [False] * 100000
    for i in a:
        print(i)
        if i == 0:
            i = 1
        pointers[(i - 1) // base] = True
    counter = 0
    for i in range(100000):
        if pointers[i]:
            counter+=1
    return counter+len(a)

print(numbersGrouping([685400881, 696804468, 696804942, 803902442, 976412678, 976414920, 47763597, 803900633, 233144924,
                       47764349, 233149077, 214990733, 214994039, 280528089, 280524347, 685401797]))
