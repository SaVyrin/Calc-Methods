import numpy.linalg

from Homework.Task5.drawer import draw_functions
from Homework.Task5.gauss_seidel import gauss_seidel_method, solve_gauss_seidel
from Homework.Task5.jacobi import jacobi_method, solve_jacobi


def sdf():
    pass


if __name__ == "__main__":
    a = [
        [0, 2, 6, 1, 1],
        [1, 19, 4, 2, 3],
        [2, 1, 10, 3, 4],
        [3, 5, 2, 20, 3],
        [4, 5, 3, 3, 12]
    ]
    b = [3, 13, 5, 12, 8]

    print(b)
    iterations_count = 40

    result_x_jacobi = solve_jacobi(a, b, iterations_count)
    result_x_gauss_seidel = solve_gauss_seidel(a, b, iterations_count)

    print(numpy.linalg.solve(a, b))

    print(result_x_jacobi)
    print(result_x_gauss_seidel)

    draw_functions(a, b)
