import numpy as np

from Homework.optimization.gradient.numerical_gradient_2_var import numerical_gradient

lr = 0.1


def adam_method(
        point, function,
        step=1e-5,
        n_max_iters=1000,
        eps=1e-7,
        beta1=0.9,
        beta2=0.999
):
    num_gradient = numerical_gradient(point, function, step)
    first_moment = np.zeros(2)
    second_moment = np.zeros(2)
    iter_ind = 1
    while np.linalg.norm(num_gradient) > eps and iter_ind < n_max_iters:
        first_moment = (beta1 * first_moment) + ((1 - beta1) * num_gradient)
        second_moment = (beta2 * second_moment) + ((1 - beta2) * num_gradient * num_gradient)
        first_unbias = first_moment / (1 - (beta1 ** iter_ind))
        second_unbias = second_moment / (1 - (beta2 ** iter_ind))
        point -= lr * first_unbias / (np.sqrt(second_unbias) + eps)
        num_gradient = numerical_gradient(point, function, step)
        iter_ind = iter_ind + 1
        # print("iter: {} grad: {}".format(iter_ind, np.linalg.norm(num_gradient)))

    return point
