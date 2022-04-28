import matplotlib.pyplot as plt
import numpy as np

from Examples.lecture_task_4.SubicSplinesSimpleApp.СubicSplinesSimpleApp.cubic_spline_3d import CubicSpline3D


def calculate_3d_spline_interpolation(x, y, z, num=100):
    cubic_spline_3d = CubicSpline3D(x, y, z)
    params = np.linspace(cubic_spline_3d.params[0], cubic_spline_3d.params[-1], num + 1)[:-1]
    # change last element to cubic_spline_3d.params[-1] last element
    # to compute value in last point
    params[-1] = cubic_spline_3d.params[-1]

    result_x, result_y, result_z = [], [], []
    for param in params:
        point_x, point_y, point_z = cubic_spline_3d.point(param)
        result_x.append(point_x)
        result_y.append(point_y)
        result_z.append(point_z)

    return result_x, result_y, result_z


if __name__ == '__main__':
    x_points = [1, 10, 3, 4, -1]
    y_points = [3, 5, 12, 5, 2]
    z_points = [-3, 0, -5, 2, 4]

    x_interpolated, y_interpolated, z_interpolated = calculate_3d_spline_interpolation(x_points, y_points, z_points)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x_points, y_points, z_points, label='linear curve')
    ax.plot(x_interpolated, y_interpolated, z_interpolated, label='cubic spline curve')

    points, = ax.plot(x_points, y_points, z_points, "x")

    plt.show()
