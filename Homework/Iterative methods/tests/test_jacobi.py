from unittest import TestCase

import numpy

from Homework.Task5.jacobi import jacobi_method


class Test(TestCase):
    def test_jacobi_method_1(self):
        a = [
            [3, 2, 1],
            [1, 5, 2],
            [2, 3, 4],
        ]
        b = [12, 3, 5]

        result_x_jacobi = [*b]

        iterations_count = 1000
        for iteration in range(iterations_count):
            result_x_jacobi = jacobi_method(a, result_x_jacobi, b)

        expected_result = numpy.linalg.solve(a, b)
        numpy.testing.assert_array_almost_equal(result_x_jacobi, expected_result)

    def test_jacobi_method_2(self):
        a = [
            [11, 2, 6, 1, 1],
            [1, 19, 4, 2, 3],
            [2, 1, 10, 3, 4],
            [3, 5, 2, 20, 3],
            [4, 5, 3, 3, 12]
        ]
        b = [3, 13, 5, 12, 8]

        result_x_jacobi = [*b]

        iterations_count = 1000
        for iteration in range(iterations_count):
            result_x_jacobi = jacobi_method(a, result_x_jacobi, b)

        expected_result = numpy.linalg.solve(a, b)
        numpy.testing.assert_array_almost_equal(result_x_jacobi, expected_result)

