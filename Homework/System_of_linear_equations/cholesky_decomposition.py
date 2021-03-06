import numpy as np


def is_pos_def(A):
    return np.all(np.linalg.eigvals(A) > 0)

def symmetric(A):
    A_Not_transp = np.array(A)
    A_transp = A_Not_transp.transpose()

    return np.allclose(A_Not_transp, A_transp)


def cholesky_decomposition(A):
    dimension_size = len(A)

    L = np.array([[0.0] * dimension_size for row in range(dimension_size)])

    for i in range(dimension_size):
        for j in range(i + 1):

            summ = sum(L[i][0:j] * L[j][0:j])

            if i == j:
                L[i][i] = (A[i][i] - summ) ** 0.5
            else:
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - summ))

    return L


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


def cholecky_solution(A, B):
    if not is_pos_def(A):
        print("Not positive definite matrix")
        return

    if not symmetric(A):
        print("Not symmetric")
        return

    L = cholesky_decomposition(A)
    U = L.transpose()

    y = forward_substitution(L, B)
    x = back_substitution(U, y)

    return x


if __name__ == "__main__":
    A = [
        [6, 15, 55],
        [15, 55, 225],
        [55, 225, 979],
    ]
    B = [76, 295, 1259]

    x = cholecky_solution(A, B)
    print(x)
