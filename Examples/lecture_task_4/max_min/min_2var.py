def function(x, y):
    return 2 * (x ** 2) + 5 * (y ** 2) + 2 * x * y - 3 * x + 4 * y - 8


def numerical_gradient(x, y, step):
    x_derivative = (function(x + step, y) - function(x - step, y)) / (2 * step)
    y_derivative = (function(x, y + step) - function(x, y - step)) / (2 * step)
    return [x_derivative, y_derivative]


def gradient_to_val(x):
    summ = 0
    for i in x:
        summ += i ** 2
    return summ ** 0.5


def find_max_min(a, b, step):
    x = a
    y = b
    gradient = numerical_gradient(x, y, step)
    gradient_val = (gradient[0] ** 2 + gradient[1] ** 2) ** 0.5
    while gradient_val > step:
        x -= gradient[0] * 0.01
        y -= gradient[1] * 0.01
        gradient = numerical_gradient(x, y, step)
        gradient_val = (gradient[0] ** 2 + gradient[1] ** 2) ** 0.5

    return [x, y]


if __name__ == "__main__":
    print(gradient_to_val([1, 4, 2]))
    print(find_max_min(5, 10, 1e-5))
