class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def ccw(A, B, C):
    return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)


def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


# a = Point(0, 0)
# b = Point(0, 1)
# c = Point(1, 1)
# d = Point(1, 0)
def robotWalk(a):
    positions = {}
    x = 0
    y = 0
    direction = 0
    positions[0, 0] = True
    lines = []
    for i in a:
        if i == 0:
            return True
        if direction % 4 == 0:
            A = Point(x, y)
            B = Point(x, y+i)
            lines.append((A, B))
            y += i

        if direction % 4 == 1:
            A = Point(x, y)
            B = Point(x+i, y)
            lines.append((A, B))
            x += i

        if direction % 4 == 2:
            A = Point(x, y)
            B = Point(x, y-i)
            lines.append((A, B))
            y -= i

        if direction % 4 == 3:
            A = Point(x, y)
            B = Point(x-i, y)
            lines.append((A, B))
            x -= i
        direction += 1

    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            result = intersect(lines[i][0], lines[i][1], lines[j][0], lines[j][1])
            if result:
                return True
    return False

print(robotWalk([7, 5, 4, 5, 2, 3]))
