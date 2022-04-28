import unittest
import gradient


class MyTestCase(unittest.TestCase):
    def test_function(self):
        actual_result = gradient.function(2, 1)
        expected_result = 1.7961172
        self.assertAlmostEqual(actual_result, expected_result, 5)

    def test_analytical_derivative(self):
        analytical_gradient = gradient.analytical_gradient(2, 1)
        actual_result = analytical_gradient[0] + analytical_gradient[1]
        expected_result = -0.9262062
        self.assertAlmostEqual(actual_result, expected_result, 5)

    def test_numerical_derivative(self):
        analytical_gradient = gradient.numerical_gradient(2, 1, 1e-5)
        actual_result = analytical_gradient[0] + analytical_gradient[1]
        expected_result = -0.9262062
        self.assertAlmostEqual(actual_result, expected_result, 5)


if __name__ == '__main__':
    unittest.main()
