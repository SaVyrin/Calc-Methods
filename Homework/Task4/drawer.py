from Homework.Task4.lagrange import LagrangeInterpolation
import matplotlib.pyplot as plt

from Homework.Task4.newton import NewtonInterpolation


def draw_function(lagrange_points, newton_points):
    lagrange_x = lagrange_points[0]
    lagrange_y = lagrange_points[-1]

    newton_x = newton_points[0]
    newton_y = newton_points[-1]

    fig, ax = plt.subplots()
    ax.plot(lagrange_x, lagrange_y, label="rectangle_integral")
    ax.plot(newton_x, newton_y, label="rectangle_integral")
    # ax.set(xlabel='x', ylabel='f', title='5 * (np.sin(x) - 3) ** 2 + 1')
    ax.grid()

    plt.show()


if __name__ == "__main__":
    x = [-1.5, -0.75, 0, 0.75, 1.5, 2.3425, 3.1, 4.0005]
    y = [-14.1014, -0.931596, 0, 0.931596, 14.1014, 3.433, 2.535, -10.424]

    lagrange = LagrangeInterpolation(x, y)
    lagrange_points = lagrange.get_result_points()
    newton = NewtonInterpolation(x, y)
    newton_points = newton.get_result_points()
    draw_function(lagrange_points, newton_points)
