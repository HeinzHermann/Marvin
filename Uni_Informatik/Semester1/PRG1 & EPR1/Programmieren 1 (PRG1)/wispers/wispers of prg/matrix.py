import random


def generate_matrix(n: int, m: int):
    if (n >= 2 and m >= 2):
        matrix = dict()
        for i in range(n):
            for j in range(m):
                matrix[(i, j)] = random.randint(0, 999999)
        matrix[(0, 0)] = random.randint(0, 9)
        matrix[(1, 0)] = random.randint(10, 99)
        matrix[(0, 1)] = random.randint(100, 999)
        matrix[(1, 1)] = random.randint(1000, 9999)
        return matrix
    else:
        raise Exception("sdah")


def print_matrix(matrix: dict):
    imax = 0
    jmax = 0
    size = 0
    for (i, j) in matrix:
        if (i > imax):
            imax = i
        if (j > jmax):
            jmax = j
        cmpsize = len(str(matrix[(i, j)]))

        size = cmpsize if cmpsize > size else size
    for i in range(imax + 1):
        print("(", end=" ")
        for j in range(jmax + 1):
            f = len(str(matrix[(i, j)]))
            print((size-f) * " ", matrix[(i, j)], sep="", end=" ")
        print(")", end="\n")

def transpose_matrix(matrix: dict):
    trans = dict()
    for (i, j) in matrix:
         trans[(j,i)] = matrix[(i,j)]
    return trans

m = generate_matrix(6, 4)
print_matrix(m)
print("\n"*2)
print_matrix(transpose_matrix(m))