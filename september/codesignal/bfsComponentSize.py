
def find_more(node_set, matrix):
    copy_dic = dict(node_set)
    for key, value in copy_dic.items():
        if not value:
            node_set[key] = True
            for j, value2 in enumerate(matrix[key]):
                if value2:
                    if j not in node_set:
                        node_set[j] = False
    if len(node_set) > len(copy_dic):
        find_more(node_set, matrix)


def bfsComponentSize(matrix):

    node_1 = {1: False}
    find_more(node_1, matrix)


    return len(node_1)

matrix = [[False, True, False],
          [True, False, False],
          [True, True, False]]

print(bfsComponentSize(matrix))
