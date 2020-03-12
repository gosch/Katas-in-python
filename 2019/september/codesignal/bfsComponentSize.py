
def find_more(n, m):
    copy_dic = dict(n)
    for k, v in copy_dic.items():
        if not v:
            n[k] = True
            for j, value2 in enumerate(m[k]):
                if value2:
                    if j not in n:
                        n[j] = False
    if len(n) > len(copy_dic):
        find_more(n, m)


def bfsComponentSize(matrix):

    node_1 = {1: False}
    find_more(node_1, matrix)
    return len(node_1)

matrix = [[False, True, False],
          [True, False, False],
          [True, True, False]]

print(bfsComponentSize(matrix))
