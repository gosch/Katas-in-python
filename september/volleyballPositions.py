def volleyballPositions(formation, k):
    positions = [formation[1][0], formation[0][1], formation[1][2],
                 formation[3][2], formation[2][1], formation[3][0]]

    k %= 6
    formation[1][0] = positions[(0 + k) % 6]
    formation[0][1] = positions[(1 + k) % 6]
    formation[1][2] = positions[(2 + k) % 6]

    formation[3][2] = positions[(3 + k) % 6]
    formation[2][1] = positions[(4 + k) % 6]
    formation[3][0] = positions[(5 + k) % 6]

    return formation


