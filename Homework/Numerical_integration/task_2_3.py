import numpy as np


def function1(x):
    return x


def function2(x):
    return 7 * (x ** 2)


def function3(x):
    return 72 * np.sin(x)


def function4(x):
    return 12 * x + x ** 3


def function5(x):
    return 3 * (x ** 4) + 7 * (x ** 2)


def gaussian_quadrature_2(a: int, b: int, function):
    f_sum = function((a + b) / 2 + (b - a) / 2 * (-0.577350)) + \
            function((a + b) / 2 + (b - a) / 2 * 0.5773503)

    result = (b - a) / 2 * f_sum
    return result


def gaussian_quadrature_3(a: int, b: int, function):
    f_sum = function((a + b) / 2 + (b - a) / 2 * -0.7745967) * 0.5555556 + \
            function((a + b) / 2) * 0.8888889 + \
            function((a + b) / 2 + (b - a) / 2 * 0.7745967) * 0.5555556

    result = (b - a) / 2 * f_sum
    return result


def gaussian_quadrature_4(a: int, b: int, function):
    f_sum = function((a + b) / 2 + (b - a) / 2 * (-0.8611363)) * 0.3478548 + \
            function((a + b) / 2 + (b - a) / 2 * (-0.3399810)) * 0.6521451 + \
            function((a + b) / 2 + (b - a) / 2 * 0.3399810) * 0.6521451 + \
            function((a + b) / 2 + (b - a) / 2 * 0.8611363) * 0.3478548

    result = (b - a) / 2 * f_sum
    return result


def gaussian_quadrature_5(a: int, b: int, function):
    f_sum = function((a + b) / 2 + (b - a) / 2 * -0.9061798) * 0.2369269 + \
            function((a + b) / 2 + (b - a) / 2 * -0.5384693) * 0.4786287 + \
            function((a + b) / 2) * 0.5688888 + \
            function((a + b) / 2 + (b - a) / 2 * 0.5384693) * 0.4786287 + \
            function((a + b) / 2 + (b - a) / 2 * 0.9061798) * 0.2369269

    result = (b - a) / 2 * f_sum
    return result


def gaussian_quadrature_6(a: int, b: int, function):
    f_sum = function((a + b) / 2 + (b - a) / 2 * (-0.9324700)) * 0.1713245 + \
            function((a + b) / 2 + (b - a) / 2 * (-0.6612094)) * 0.3607616 + \
            function((a + b) / 2 + (b - a) / 2 * (-0.2386142)) * 0.4679140 + \
            function((a + b) / 2 + (b - a) / 2 * 0.2386142) * 0.4679140 + \
            function((a + b) / 2 + (b - a) / 2 * 0.6612094) * 0.3607616 + \
            function((a + b) / 2 + (b - a) / 2 * 0.9324700) * 0.1713245

    result = (b - a) / 2 * f_sum
    return result


if __name__ == '__main__':
    a = 0
    b = 3

    functions = [function1, function2, function3, function4, function5]

    for function in functions:
        print(function.__name__)
        print("Метод Гаусса(2): {}".format(
            gaussian_quadrature_2(a, b, function)))
        print("Метод Гаусса(3): {}".format(
            gaussian_quadrature_3(a, b, function)))
        print("Метод Гаусса(4): {}".format(
            gaussian_quadrature_4(a, b, function)))
        print("Метод Гаусса(5): {}".format(
            gaussian_quadrature_5(a, b, function)))
        print("Метод Гаусса(6): {}".format(
            gaussian_quadrature_6(a, b, function)))
        print()
