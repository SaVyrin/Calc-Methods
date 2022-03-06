import numpy as np
import matplotlib.pyplot as plt


def function(x):
    return 3 * (x ** 4) + 7 * (x ** 2)


def rectangle_integral(a: int, b: int, count: int):
    h = (b - a) / count
    y_sum = 0.0
    for curr_iter in range(0, count):
        x = a + h * curr_iter
        y_sum += function(x)

    result = h * y_sum
    return result


def trapezoid_integral(a: int, b: int, count: int):
    h = (b - a) / count

    y_sum = function(a) + function(b)
    for curr_iter in range(1, count - 2):
        x = a + h * curr_iter
        y_sum += 2 * function(x)

    result = h / 2 * y_sum
    return result


def parabolic_integral(a: int, b: int, count: int):
    h = (b - a) / count

    y_sum = function(a)
    if count % 2 == 0:
        y_sum += function(b)

    for curr_iter in range(1, count, 2):
        x = a + h * curr_iter
        y_sum += 4 * function(x)

    for curr_iter in range(2, count - 1, 2):
        x = a + h * curr_iter
        y_sum += 2 * function(x)

    result = h / 3 * y_sum
    return result


def cube_parabolic_integral(a: int, b: int, count: int):
    h = (b - a) / count

    y_sum = function(a) + function(b)
    for curr_iter in range(1, count - 1, 3):
        x = a + h * curr_iter
        y_sum += 3 * function(x)

    for curr_iter in range(2, count - 1, 3):
        x = a + h * curr_iter
        y_sum += 3 * function(x)

    for curr_iter in range(3, count - 1, 3):
        x = a + h * curr_iter
        y_sum += 2 * function(x)

    result = 3 / 8 * h * y_sum
    return result


def bul_integral(a: int, b: int, count: int):
    h = (b - a) / count

    y_sum = 7 * function(a) + 7 * function(b)
    for curr_iter in range(1, count - 1, 2):
        x = a + h * curr_iter
        y_sum += 32 * function(x)

    for curr_iter in range(2, count - 1, 4):
        x = a + h * curr_iter
        y_sum += 12 * function(x)

    for curr_iter in range(4, count - 1, 4):
        x = a + h * curr_iter
        y_sum += 14 * function(x)

    result = 2 / 45 * h * y_sum
    return result


def draw_functions():
    x_arr = np.arange(1, 50)

    expected_result = 208.8
    f1 = []
    f2 = []
    f3 = []
    f4 = []
    f5 = []

    for x in x_arr:
        f1.append(abs(rectangle_integral(0, 3, x) - expected_result))
        f2.append(abs(trapezoid_integral(0, 3, x) - expected_result))
        f3.append(abs(parabolic_integral(0, 3, x) - expected_result))
        f4.append(abs(cube_parabolic_integral(0, 3, x) - expected_result))
        f5.append(abs(bul_integral(0, 3, x) - expected_result))

    fig, ax = plt.subplots()
    ax.plot(x_arr, f1, label="rectangle_integral")
    ax.plot(x_arr, f2, label="trapezoid_integral")
    ax.plot(x_arr, f3, label="parabolic_integral")
    ax.plot(x_arr, f4, label="cube_parabolic_integral")
    ax.plot(x_arr, f5, label="bul_integral", )

    ax.set(xlabel='x', ylabel='f', title='3 * (x ** 4) + 7 * (x ** 2)')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)
    ax.grid()

    plt.show()


if __name__ == '__main__':
    a = 0
    b = 3
    step = 100000
    draw_functions()

    print("Метод прямоугольников: {}".format(
        rectangle_integral(a, b, step)))

    print("Метод трапеций: {}".format(
        trapezoid_integral(a, b, step)))

    print("Метод парабол (Симпсона): {}".format(
        parabolic_integral(a, b, step)))

    print("Метод кубических парабол: {}".format(
        cube_parabolic_integral(a, b, step)))

    print("Метод Буля: {}".format(
        bul_integral(a, b, step)))
