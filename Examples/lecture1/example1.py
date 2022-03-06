import numpy as np
import matplotlib.pyplot as plt


def function(x):
    return 5 * (np.sin(x) - 3) ** 2 + 1


def analytical_derivative(x):
    return 10 * np.cos(x) * (np.sin(x) - 3)


def numerical_derivative(x, step):
    return (function(x + step) - function(x - step)) / (2 * step)


def draw_function():
    x = np.arange(-5.0, 5.0, 0.01)
    f = function(x)

    fig, ax = plt.subplots()
    ax.plot(x, f)
    ax.set(xlabel='x', ylabel='f', title='5 * (np.sin(x) - 3) ** 2 + 1')
    ax.grid()

    plt.show()


if __name__ == '__main__':
    x = 2.5
    step = 1e-5

    draw_function()

    print("function value at x = {0} is {1}".format(x, function(x)))
    print("analytical derivative value at x = {0} is {1}".format(x, analytical_derivative(x)))
    print("numerical derivative value at x = {0} with step = {1} is {2}".format(x, step, numerical_derivative(x, step)))



