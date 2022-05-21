import numpy
import numpy as np
from multipledispatch import dispatch


@dispatch(int, int, object, float)
def numerical_gradient(x, y, function, step):
    x_derivative = (function(x + step, y) - function(x - step, y)) / (2 * step)
    y_derivative = (function(x, y + step) - function(x, y - step)) / (2 * step)
    return np.array([x_derivative, y_derivative])


@dispatch(float, float, object, float)
def numerical_gradient(x, y, function, step):
    x_derivative = (function(x + step, y) - function(x - step, y)) / (2 * step)
    y_derivative = (function(x, y + step) - function(x, y - step)) / (2 * step)
    return np.array([x_derivative, y_derivative])


@dispatch(numpy.ndarray, object, float)
def numerical_gradient(point, function, step):
    x_derivative = (function(point[0] + step, point[1]) - function(point[0] - step, point[1])) / (2 * step)
    y_derivative = (function(point[0], point[1] + step) - function(point[0], point[1] - step)) / (2 * step)
    return np.array([x_derivative, y_derivative])
