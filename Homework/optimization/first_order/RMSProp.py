import numpy as np

from Homework.optimization.gradient.numerical_gradient_2_var import numerical_gradient

lr = 0.7


def rmsprop_method(
        point, function,
        step=1e-5,
        n_max_iters=1000,
        eps=1e-7,
        decay=0.5
):
    num_gradient = numerical_gradient(point, function, step)
    grad_squared = np.zeros(2)
    iter_ind = 0
    while np.linalg.norm(num_gradient) > eps and iter_ind < n_max_iters:
        grad_squared += (decay * grad_squared) + ((1 - decay) * num_gradient * num_gradient)
        point -= lr * num_gradient / (np.sqrt(grad_squared) + eps)
        num_gradient = numerical_gradient(point, function, step)
        iter_ind = iter_ind + 1
        # print("iter: {} grad: {}".format(iter_ind, np.linalg.norm(num_gradient)))

    return point
