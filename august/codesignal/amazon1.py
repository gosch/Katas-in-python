def ClosestXdestination(numDestinations, allLocations, numDeliveries):



    distances = []
    for i in range(numDestinations):

        distances.append([allLocations[i], allLocations[i][0] ** 2 + allLocations[i][1] ** 2])
    distances.sort(key=lambda e:e[1])
    return [distances[i][0] for i in range(numDeliveries)]

print(ClosestXdestination(3, [[1, 2], [3, 4], [1, -1]], 2))

