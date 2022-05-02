import logging


def gauss_seidel_method(a, x, b):
    result_x = [*x]
    equations_count = len(b)
    for equation_number in range(equations_count):
        elements_sum = 0.0
        for sum_equation_number in range(equations_count):
            if sum_equation_number != equation_number:
                elements_sum += a[equation_number][sum_equation_number] * result_x[sum_equation_number]

        new_x = (b[equation_number] - elements_sum) / a[equation_number][equation_number]
        result_x[equation_number] = new_x

    return result_x


def solve_gauss_seidel(a, b, iterations_count=100):
    result_x_gauss_seidel = [*b]
    try:
        for iteration in range(iterations_count):
            result_x_gauss_seidel = gauss_seidel_method(a, result_x_gauss_seidel, b)
    except ZeroDivisionError as e:
        logging.error("Zeros in diagonal")

    return result_x_gauss_seidel
