import numpy as np


def cholesky_decomposition(A, L):
    dimension_size = len(A)

    for i in range(dimension_size):
        for j in range(i + 1):

            summ = sum(L[i][0:j] * L[j][0:j])

            if i == j:
                L[i][i] = (A[i][i] - summ) ** 0.5
            else:
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - summ))


def forward_substitution(L, B):
    n = len(B)

    y = [0 for i in range(n)]
    for i in range(n):
        summ = sum(L[i][0:i] * y[0:i])
        y[i] = (B[i] - summ) / L[i][i]
    return y


def back_substitution(U, Y):
    n = len(Y)

    x = [0 for i in range(n)]
    for i in range(-1, -n - 1, -1):
        summ = sum(U[i][i:] * x[i:])
        x[i] = (Y[i] - summ) / U[i][i]
    return x


if __name__ == "__main__":
    A = [
        [6, 15, 55],
        [15, 55, 225],
        [55, 225, 979],
    ]
    B = [76, 295, 1259]
    L = np.array([
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0],
    ])
    cholesky_decomposition(A, L)
    U = L.transpose()
    print(L)
    print(U)
    y = forward_substitution(L, B)
    print(y)
    x = back_substitution(U, y)
    print(x)
