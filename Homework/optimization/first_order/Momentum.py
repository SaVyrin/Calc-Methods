import numpy as np

from Homework.optimization.gradient.numerical_gradient_2_var import numerical_gradient

lr = 0.01


def momentum_method(
        point, function,
        step=1e-5,
        n_max_iters=1000,
        eps=1e-7,
        decay=0.9
):
    num_gradient = numerical_gradient(point, function, step)
    momentum = np.zeros(2)
    iter_ind = 0
    while np.linalg.norm(num_gradient) > eps and iter_ind < n_max_iters:
        momentum = (decay * momentum) + (lr * num_gradient)
        point -= momentum
        num_gradient = numerical_gradient(point, function, step)
        iter_ind = iter_ind + 1
        # print("iter: {} grad: {}".format(iter_ind, np.linalg.norm(num_gradient)))

    return point
