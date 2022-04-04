import numpy as np


class LagrangeInterpolation:
    def __init__(self, given_x, given_y):
        self._given_x = given_x
        self._given_y = given_y
        self._interpolation_points_count = 10000

    def get_result_points(self):
        result_x, result_y = self._interpolate()
        return result_x, result_y

    def _get_interpolated_y(self, x):
        given_points_count = len(self._given_x)
        result_y = 0
        for current_x_index in range(given_points_count):

            sub_result = 1
            for other_x_index in range(given_points_count):
                if not current_x_index == other_x_index:
                    sub_result *= (x - self._given_x[other_x_index]) \
                                  / (self._given_x[current_x_index] - self._given_x[other_x_index])

            result_y += self._given_y[current_x_index] * sub_result

        return result_y

    def _interpolate(self):
        interpolation_y_values = []
        interpolation_x_values = np.linspace(self._given_x[0], self._given_x[-1], self._interpolation_points_count)
        for x in interpolation_x_values:
            interpolation_y_values.append(self._get_interpolated_y(x))

        return interpolation_x_values, interpolation_y_values
