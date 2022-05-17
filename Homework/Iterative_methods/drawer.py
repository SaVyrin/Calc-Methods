import numpy as np
from matplotlib import pyplot as plt

from Homework.Iterative_methods.gauss_seidel import solve_gauss_seidel
from Homework.Iterative_methods.jacobi import solve_jacobi


def get_error_value(actual_result, expected_result):
    total_error = 0
    iterations_count = len(actual_result)
    for iteration in range(iterations_count):
        error = abs(expected_result[iteration] - actual_result[iteration])
        total_error += error
    return total_error


def draw_functions(a, b):
    x_arr = np.arange(1, 50)

    expected_result = np.linalg.solve(a, b)
    f_jacobi = []
    f_gauss_seidel = []

    for x in x_arr:
        result_x_jacobi = solve_jacobi(a, b, x)
        jacobi_error = get_error_value(result_x_jacobi, expected_result)
        f_jacobi.append(jacobi_error)

        result_x_gauss_seidel = solve_gauss_seidel(a, b, x)
        gauss_seidel_error = get_error_value(result_x_gauss_seidel, expected_result)
        f_gauss_seidel.append(gauss_seidel_error)

    fig, ax = plt.subplots()
    ax.plot(x_arr, f_jacobi, label="jacobi method")
    ax.plot(x_arr, f_gauss_seidel, label="gauss seidel method")

    ax.set(xlabel='x', ylabel='f', title='iterative methods')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)
    ax.grid()

    plt.show()
