from Homework.Task4.lagrange import LagrangeInterpolation
import matplotlib.pyplot as plt


def draw_function(points):
    x = points[0]
    f = points[-1]

    fig, ax = plt.subplots()
    ax.plot(x, f)
    # ax.set(xlabel='x', ylabel='f', title='5 * (np.sin(x) - 3) ** 2 + 1')
    ax.grid()

    plt.show()


if __name__ == "__main__":
    x = [-1.5, -0.75, 0, 0.75, 1.5]
    y = [-14.1014, -0.931596, 0, 0.931596, 14.1014]

    lagrange = LagrangeInterpolation(x, y)
    points = lagrange.get_result_points()
    draw_function(points)
