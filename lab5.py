def sum_matrix(a, b):
    c = [[0] * len(a[0]) for i in a]

    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] + b[i][j]

    return c


def prod_matrix_with_vector(a, b):
    c = [[0] * len(a[0]) for i in a]

    for i in range(len(a)):
        c[i] = 0
        for j in range(len(a[i])):
            c[i] += a[i][j] * b[j]

    return c


def prod_matrix(a, b):
    c = [[0] * len(a[0]) for i in a]

    for i in range(len(a)):
        c[i] = 0
        for j in range(len(a[i])):
            c[i] += a[i][j] * b[i][j]

    return c


def is_simetric(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != a[j][i]:
                return 0

    return 1

print "Suma matrici: ", \
        sum_matrix(
                    [
                        [1, 2],
                        [3, 4],
                        [5, 6]
                    ],
                    [
                        [2, -1],
                        [-7, 6],
                        [11, -11]
                    ]
                ), "\n"

print "Produs: ", \
        prod_matrix_with_vector(
            [
                [2, 1, 3],
                [4, 7, 9]
            ],
            [1, 2, 3]
        ), "\n"
