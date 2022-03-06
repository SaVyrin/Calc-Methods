import numpy as np
import matplotlib.pyplot as plt

'''   function
    3 * sin(1.2^y) - log2(x^3) + x
'''


def function(x, y):
    return 3 * np.sin(1.2 ** y) - np.log2(x ** 3) + x


'''   function derivative
    (6^y) * cos((6^y) / (5^y)) * (3*ln(6) - 3 * ln(5)) / (5^y) - 3 / (ln(2)*x) + 1
'''


def analytical_gradient(x, y):
    x_derivative = - 3 / (np.log(2) * x) + 1
    y_derivative = (6 ** y) * np.cos((6 ** y) / (5 ** y)) * (3 * np.log(6) - 3 * np.log(5)) / (5 ** y)
    return [x_derivative, y_derivative]


def numerical_gradient(x, y, step):
    x_derivative = (function(x + step, y) - function(x - step, y)) / (2 * step)
    y_derivative = (function(x, y + step) - function(x, y - step)) / (2 * step)
    return [x_derivative, y_derivative]


def draw_3d_function():
    x, y = np.meshgrid(np.linspace(2, 10, 25), np.linspace(2, 10, 25))
    z = function(x, y)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.plot_surface(x, y, z, cmap='inferno')
    ax.set(xlabel="x", ylabel="y", zlabel="z", title="3 * sin(1.2^y) - log2(x^3) + x")
    ax.legend()

    plt.show()


if __name__ == '__main__':
    x = 2.5
    y = 2.5
    step = 1e-5

    draw_3d_function()

    print("function value at x = {0} and y = {1} is {2}".format(x, y, function(x, y)))

    analytical_gradient = analytical_gradient(x, y)
    print("analytical derivative value at x = {0} and y = {1} is {2}".format(
        x, y, analytical_gradient))

    numerical_gradient = numerical_gradient(x, y, step)
    print("numerical derivative value at x = {0} and y = {1} with step = {2} is {3}".format(
        x, y, step, numerical_gradient))
