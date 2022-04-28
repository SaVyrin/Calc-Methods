import random


def function(x):
    return 3 * (x ** 4) + 7 * (x ** 2)


def function_2var(x, y):
    return 3 * (x ** 4) + 7 * (y ** 2)


def monte_carlo_method(a: int, b: int, count: int):
    h = (b - a) / count

    y_sum = 0.0
    for curr_iter in range(0, count):
        x = random.uniform(a, b)
        y_sum += function(x)

    result = h * y_sum
    return result


def monte_carlo_method_2var(ax: int, bx: int, ay: int, by: int, count: int):
    dx = (bx - ax) / count
    dy = (by - ay) / count

    f_sum = 0.0
    for i in range(0, count):
        for j in range(0, count):
            x = random.uniform(ax, bx)
            y = random.uniform(ay, by)
            f_sum += function_2var(x, y)

    result = (dx * dy) * f_sum
    return result


def trapezoidal_integral_2var(ax: int, bx: int, ay: int, by: int, count: int):
    dx = (bx - ax) / count
    dy = (by - ay) / count

    f_sum = function_2var(ax, ay) + \
            function_2var(bx, ay) + \
            function_2var(ax, by) + \
            function_2var(bx, by)
    for i in range(1, count - 1):
        for j in range(1, count - 1):
            x = ax + dx * i
            y = ay + dy * j
            f_sum += 2 * function_2var(x, y)

    result = (dx * dy) / 2 * f_sum
    return result


if __name__ == '__main__':
    a = 0
    b = 3
    count = 100000

    print("Метод Монте-Карло: {}".format(
        monte_carlo_method(a, b, count)))
    print("Метод Монте-Карло для 2х переменных: {}".format(
        monte_carlo_method_2var(0, 2, 0, 1, 500)))
    print("Метод трапеций для 2х переменных: {}".format(
        trapezoidal_integral_2var(0, 2, 0, 1, 500)))
