from unittest import TestCase

import numpy.testing

from Homework.Iterative_methods.gauss_seidel import gauss_seidel_method


class Test(TestCase):
    def test_seidel_method_1(self):
        a = [
            [3, 2, 1],
            [1, 5, 2],
            [2, 3, 4],
        ]
        b = [12, 3, 5]

        result_x_gauss_seidel = [*b]

        iterations_count = 1000
        for iteration in range(iterations_count):
            result_x_gauss_seidel = gauss_seidel_method(a, result_x_gauss_seidel, b)

        expected_result = numpy.linalg.solve(a, b)
        numpy.testing.assert_array_almost_equal(result_x_gauss_seidel, expected_result)

    def test_seidel_method_2(self):
        a = [
            [11, 2, 6, 1, 0],
            [0, 9, 4, 2, 8],
            [2, 8, 11, 6, 4],
            [3, 5, 7, 10, 3],
            [8, 5, 3, 3, 12]
        ]
        b = [12, 3, 5, 5, 4]

        result_x_gauss_seidel = [*b]

        iterations_count = 1000
        for iteration in range(iterations_count):
            result_x_gauss_seidel = gauss_seidel_method(a, result_x_gauss_seidel, b)

        expected_result = numpy.linalg.solve(a, b)
        numpy.testing.assert_array_almost_equal(result_x_gauss_seidel, expected_result)
