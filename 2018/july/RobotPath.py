def robotPath(instructions, bound):
    x_position = 0
    y_position = 0
    for step in instructions:
        if step == 'L':
            if x_position == -bound:
                continue
            x_position = x_position - 1
        elif step == 'R':
            if x_position == bound:
                continue
            x_position = x_position + 1
        elif step == 'U':
            if y_position == bound:
                continue
            y_position = y_position + 1
        else:
            if y_position == -bound:
                continue
            y_position = y_position - 1
    return [x_position, y_position]
