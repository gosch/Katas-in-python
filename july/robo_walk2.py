def robotWalk(a):
    direction = 3
    top_x = a[1]
    top_y = a[2]
    for i in range(3, len(a)):
        if direction % 4 == 0:
            if a[i] >= top_y:
                return True
            top_y = a[i]
        if direction % 4 == 1:
            if a[i] >= top_x:
                return True
            top_x = a[i]
        if direction % 4 == 2:
            if a[i] >= top_y:
                return True
            top_y = a[i]
        if direction % 4 == 3:
            if a[i] >= top_x:
                return True
            top_x = a[i]
        direction += 1

    return False

print(robotWalk([10, 3, 10, 2, 5, 1, 2]))
