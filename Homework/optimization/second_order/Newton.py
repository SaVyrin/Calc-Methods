import numpy as np

from Homework.optimization.gradient.numerical_gradient_2_var import numerical_gradient

lr = 0.01


def derivative_xx(x, y):
    return 2


def derivative_xy(x, y):
    return 0


def derivative_yy(x, y):
    return 2


def is_pos_def(A):
    print(np.linalg.eigvals(A))
    return np.all(np.linalg.eigvals(A) > 0)


def newton_method(
        point, function,
        step=1e-5,
        n_max_iters=1000,
        eps=1e-7,
):
    num_gradient = numerical_gradient(point, function, step)
    iter_ind = 0
    while np.linalg.norm(num_gradient) > eps and iter_ind < n_max_iters:
        der_xx = derivative_xx(point[0], point[1])
        der_xy = derivative_xy(point[0], point[1])
        der_yy = derivative_yy(point[0], point[1])
        matrix = np.matrix([
            [der_xx, der_xy],
            [der_xy, der_yy]
        ])
        if is_pos_def(matrix):
            print(np.linalg.solve(matrix, -num_gradient))
            point += np.linalg.solve(matrix, -num_gradient)
        else:
            point -= lr * num_gradient

        num_gradient = numerical_gradient(point, function, step)
        iter_ind = iter_ind + 1
        # print("iter: {} grad: {}".format(iter_ind, np.linalg.norm(num_gradient)))

    return point
