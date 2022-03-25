from unittest import TestCase
import numpy as np
import numpy.testing

from Homework.Task3.tridiagonal_matrix_algorithm import tdma_solve


class TestTDMA(TestCase):
    def test_tdma_solve1(self):
        a = [0, 1, 3, 6, 6]
        b = [1, 4, 2, 3, 2]
        c = [8, 2, 2, 1, 0]
        d = [1, 5, 3, 4, 7]

        actual = np.array(tdma_solve(a, b, c, d))

        matrix_np = np.array([
            [1, 8, 0, 0, 0],
            [1, 4, 2, 0, 0],
            [0, 3, 2, 2, 0],
            [0, 0, 6, 3, 1],
            [0, 0, 0, 6, 2],
        ])
        sol_np = np.array([1, 5, 3, 4, 7])

        expected = np.linalg.solve(matrix_np, sol_np)

        print(actual)
        print(expected)

        numpy.testing.assert_array_almost_equal(actual, expected)

    def test_tdma_solve2(self):
        a = [0, 1, 3, 6, 6, 2]
        b = [1, 4, 2, 3, 2, 5]
        c = [8, 2, 2, 1, 3, 0]
        d = [1, 5, 3, 4, 7, 6]

        actual = np.array(tdma_solve(a, b, c, d))

        matrix_np = np.array([
            [1, 8, 0, 0, 0, 0],
            [1, 4, 2, 0, 0, 0],
            [0, 3, 2, 2, 0, 0],
            [0, 0, 6, 3, 1, 0],
            [0, 0, 0, 6, 2, 3],
            [0, 0, 0, 0, 2, 5],
        ])
        sol_np = np.array([1, 5, 3, 4, 7, 6])

        expected = np.linalg.solve(matrix_np, sol_np)

        print(actual)
        print(expected)

        np.testing.assert_array_almost_equal(actual, expected)
