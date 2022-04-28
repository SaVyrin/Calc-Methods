import numpy as np


class NewtonInterpolation:
    def __init__(self, given_x, given_y):
        self._given_x = given_x
        self._given_y = given_y
        self._interpolation_points_count = 500

    def get_result_points(self):
        result_x, result_y = self._interpolate()
        return result_x, result_y

    def _divided_difference(self, n):
        result_difference = 0
        for current_x_index in range(n):

            sub_difference_denominator = 1
            for other_x_index in range(n):
                if not current_x_index == other_x_index:
                    sub_difference_denominator *= self._given_x[current_x_index] - self._given_x[other_x_index]

            result_difference += self._given_y[current_x_index] / sub_difference_denominator

        return result_difference

    def _get_interpolated_y(self, x):
        given_points_count = len(self._given_x)
        result_y = self._given_y[0]
        multiply_of_x_difference = 1
        for current_iteration in range(given_points_count - 1):
            multiply_of_x_difference *= (x - self._given_x[current_iteration])
            result_y += self._divided_difference(current_iteration + 2) * multiply_of_x_difference

        return result_y

    def _interpolate(self):
        interpolation_y_values = []
        interpolation_x_values = np.linspace(self._given_x[0], self._given_x[-1], self._interpolation_points_count)
        for x in interpolation_x_values:
            interpolation_y_values.append(self._get_interpolated_y(x))

        return interpolation_x_values, interpolation_y_values
