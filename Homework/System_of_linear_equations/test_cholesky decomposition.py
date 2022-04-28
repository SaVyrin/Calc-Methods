from unittest import TestCase

import numpy as np

from Homework.System_of_linear_equations.cholesky_decomposition import cholesky_decomposition, cholecky_solution


class Test(TestCase):
    def test_cholesky_decomposition(self):
        A = [
            [6, 15, 55],
            [15, 55, 225],
            [55, 225, 979],
        ]

        actual = np.array(cholesky_decomposition(A))
        expected = np.linalg.cholesky(np.array(A))

        print(actual)
        print(expected)

        np.testing.assert_array_almost_equal(actual, expected)

    def test_cholesky_decomposition2(self):
        A = [
            [1, 2, 3, 4, 5],
            [2, 20, 7, 8, 9],
            [3, 7, 40, 11, 12],
            [4, 8, 11, 60, 14],
            [5, 9, 12, 14, 100],
        ]

        actual = np.array(cholesky_decomposition(A))
        expected = np.linalg.cholesky(np.array(A))

        print(actual)
        print(expected)

        np.testing.assert_array_almost_equal(actual, expected)

    def test_cholecky_solution(self):
        A = [
            [6, 15, 55],
            [15, 55, 225],
            [55, 225, 979],
        ]
        B = [76, 295, 1259]

        actual = np.array(cholecky_solution(A, B))
        expected = np.linalg.solve(np.array(A), np.array(B))

        print(actual)
        print(expected)

        np.testing.assert_array_almost_equal(actual, expected)

    def test_cholecky_solution2(self):
        A = [
            [1, 2, 3, 4, 5],
            [2, 20, 7, 8, 9],
            [3, 7, 40, 11, 12],
            [4, 8, 11, 60, 14],
            [5, 9, 12, 14, 100],
        ]
        B = [35, 75, 125, 225, 450]

        actual = np.array(cholecky_solution(A, B))
        expected = np.linalg.solve(np.array(A), np.array(B))

        print(actual)
        print(expected)

        np.testing.assert_array_almost_equal(actual, expected)
