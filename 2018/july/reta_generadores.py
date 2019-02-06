def robotWalk(a):
    positions = {}
    x = 0
    y = 0
    direction = 0
    positions[0, 0] = True
    for i in a:
        if i == 0:
            return True
        if direction % 4 == 0:
            for j in range(1, i + 1):
                if (x, y + j) in positions:
                    return True
                else:
                    positions[(x, y + j)] = True
            y += i
        if direction % 4 == 1:
            for j in range(1, i + 1):
                if (x + j, y) in positions:
                    return True
                else:
                    positions[(x + j, y)] = True
            x += i

        if direction % 4 == 2:
            for j in range(1, i + 1):
                if (x, y - j) in positions:
                    return True
                else:
                    positions[(x, y - j)] = True
            y -= i

        if direction % 4 == 3:
            for j in range(1, i + 1):
                if (x - j, y) in positions:
                    return True
                else:
                    positions[(x - j, y)] = True
            x -= i
        direction += 1
    return False





print(robotWalk([7, 5, 4, 5, 2, 3]))
