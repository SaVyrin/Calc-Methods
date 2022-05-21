import numpy as np

from Homework.optimization.gradient.numerical_gradient_2_var import numerical_gradient

lr = 0.01


def gradient_descent(
        point, function,
        step=1e-5,
        n_max_iters=1000,
        eps=1e-7
):
    iter_ind = 0
    num_gradient = numerical_gradient(point, function, step)
    while np.linalg.norm(num_gradient) > eps and iter_ind < n_max_iters:
        point -= lr * num_gradient
        num_gradient = numerical_gradient(point, function, step)
        iter_ind = iter_ind + 1
        # print("iter: {} grad: {}".format(iter_ind, np.linalg.norm(num_gradient)))

    return point
