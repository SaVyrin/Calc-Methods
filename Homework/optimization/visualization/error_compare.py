import numpy as np
from matplotlib import pyplot as plt

from Homework.optimization.first_order.AdaGrad import adagrad_method
from Homework.optimization.first_order.Adam import adam_method
from Homework.optimization.first_order.GradientDescent import gradient_descent
from Homework.optimization.first_order.Momentum import momentum_method
from Homework.optimization.first_order.NesterovMomentum import nesterov_momentum_method
from Homework.optimization.first_order.RMSProp import rmsprop_method
from Homework.optimization.second_order.Newton import newton_method


def get_error_value(actual_result, expected_result):
    total_error = 0
    elements_count = len(actual_result)
    for curr_idx in range(elements_count):
        error = abs(expected_result[curr_idx] - actual_result[curr_idx])
        total_error += error
    return total_error


def append_error_function(error_function, start_point, function, optimization_function, steps_count, expected_result):
    result = optimization_function(start_point, function, n_max_iters=steps_count)
    error = get_error_value(result, expected_result)
    return error_function.append(error)


def draw_functions(start_x, start_y, function, expected_result):
    x_steps_count = np.arange(1, 50)

    f_gradient_descent = []
    f_momentum = []
    f_nesterov_momentum = []
    f_adagrad = []
    f_rmsprop = []
    f_adam = []
    f_newton = []

    for current_steps_count in x_steps_count:
        append_error_function(f_gradient_descent, np.array([start_x, start_y]),
                              function, gradient_descent,
                              current_steps_count, expected_result)

        append_error_function(f_momentum, np.array([start_x, start_y]),
                              function, momentum_method,
                              current_steps_count, expected_result)

        append_error_function(f_nesterov_momentum, np.array([start_x, start_y]),
                              function, nesterov_momentum_method,
                              current_steps_count, expected_result)

        append_error_function(f_adagrad, np.array([start_x, start_y]),
                              function, adagrad_method,
                              current_steps_count, expected_result)

        append_error_function(f_rmsprop, np.array([start_x, start_y]),
                              function, rmsprop_method,
                              current_steps_count, expected_result)

        append_error_function(f_adam, np.array([start_x, start_y]),
                              function, adam_method,
                              current_steps_count, expected_result)

        append_error_function(f_newton, np.array([start_x, start_y]),
                              function, newton_method,
                              current_steps_count, expected_result)

    fig, ax = plt.subplots()
    ax.plot(x_steps_count, f_gradient_descent, label="Gradient descent")
    ax.plot(x_steps_count, f_momentum, label="Momentum")
    ax.plot(x_steps_count, f_nesterov_momentum, label="Nesterov momentum")
    ax.plot(x_steps_count, f_adagrad, label="AdaGrad")
    ax.plot(x_steps_count, f_rmsprop, label="RMSProp")
    ax.plot(x_steps_count, f_adam, label="Adam")
    ax.plot(x_steps_count, f_newton, label="Newton")

    ax.set(xlabel='Steps count', ylabel='Error value', title='Optimization methods')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)
    ax.grid()

    plt.show()
