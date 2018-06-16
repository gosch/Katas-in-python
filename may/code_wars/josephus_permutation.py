def generate_josephus_permutation(permute):
    pointer = 3
    elements_removed = []
    while not permute:
        permute.remove(permute[pointer])



