def function(x):
    return (x ** 3) - 100 * (x ** 2) + x


def function_derivative(x):
    return 3 * (x ** 2) - (200 * x) + 1


def find_max_min(a):
    x = a

    derivative = function_derivative(x)
    if derivative > 0:
        while derivative > 0:
            x -= 0.01
            derivative = function_derivative(x)
    else:
        while derivative < 0:
            x += 0.01
            derivative = function_derivative(x)

    return x


if __name__ == "__main__":
    print(find_max_min(4))
