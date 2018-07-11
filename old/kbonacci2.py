def expo(matrix, power, identity):
    if power == 0:
        return identity
    elif power == 1:
        return matrix
    elif power & 1:
        return multiply(matrix, expo(matrix, power - 1, identity))
    else:
        x = expo(matrix, power >> 1, identity)
        return multiply(x, x)


def multiply(A, B):
    ret = [list() for i in range(len(B))]
    for i, row in enumerate(B):
        for j in range(len(A[0])):
            coloumn = (r[j] for r in A)
            ret[i].append(vector_multiply(row, coloumn))
    return ret


def vector_multiply(X, Y):
    return sum(a * b for (a, b) in zip(X, Y))


def fibonacci(n, k=2):
    start = [[1] * k]
    identity = [[1 if col == row else 0 for col in range(k)] for row in range(k)]  # identity matrix
    # build the matrix for k
    matrix = [[1] * k]
    for i in range(1, k):
        matrix.append([0] * (i - 1) + [1] + [0] * (k - i))
    r = expo(matrix, n - 1, identity)
    return multiply(start, r)[0][0]



print(fibonacci(100_000, k=16))
