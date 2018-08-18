def insideCircle(point, center, radius):
    dis = (center[0] - point[0])**2 + (center[1] - point[1])**2 ** 1//2
    return radius <= dis

point = [1, 1]
center = [2, 2]
radius = 1

print(insideCircle(point, center, radius))
