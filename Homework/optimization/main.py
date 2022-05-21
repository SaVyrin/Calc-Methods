import numpy as np

from Homework.optimization.first_order.AdaGrad import adagrad_method
from Homework.optimization.first_order.Adam import adam_method
from Homework.optimization.first_order.GradientDescent import gradient_descent
from Homework.optimization.first_order.Momentum import momentum_method
from Homework.optimization.first_order.NesterovMomentum import nesterov_momentum_method
from Homework.optimization.first_order.RMSProp import rmsprop_method
from Homework.optimization.second_order.Newton import newton_method
from Homework.optimization.visualization.error_compare import draw_functions


def function(x, y):
    return (x ** 2) + (y ** 2)


if __name__ == "__main__":
    start_x = 1.0
    start_y = 1.0
    step = 1e-5
    n_max_iters = 1500
    eps = 1e-7

    expected_result = (0.0, 0.0)

    draw_functions(start_x, start_y, function, expected_result)

    minimum1 = gradient_descent(np.array([start_x, start_y]), function, step, n_max_iters, eps)
    minimum2 = momentum_method(np.array([start_x, start_y]), function, step, n_max_iters, eps)
    minimum3 = nesterov_momentum_method(np.array([start_x, start_y]), function, step, n_max_iters, eps)
    minimum4 = adagrad_method(np.array([start_x, start_y]), function, step, n_max_iters, eps)
    minimum5 = rmsprop_method(np.array([start_x, start_y]), function, step, n_max_iters, eps)
    minimum6 = adam_method(np.array([start_x, start_y]), function, step, n_max_iters, eps)
    minimum7 = newton_method(np.array([start_x, start_y]), function, step, n_max_iters, eps)
    print(f'{minimum1} - gradient descent')
    print(f'{minimum2} - momentum:')
    print(f'{minimum3} - nesterov momentum')
    print(f'{minimum4} - adagrad')
    print(f'{minimum5} - rmsprop')
    print(f'{minimum6} - adam')
    print(f'{minimum7} - newton')
