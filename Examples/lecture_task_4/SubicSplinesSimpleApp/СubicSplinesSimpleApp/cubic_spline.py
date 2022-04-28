import numpy as np
import bisect

from Homework.System_of_linear_equations.tridiagonal_matrix_algorithm import tdma_solve


class CubicSpline:
    def __init__(self, x, y):
        self.b, self.c, self.d = [], [], []
        self.x = x
        self.y = y

        h = np.diff(x)
        # checking for zero values and replacing them with epsilon
        # to avoid division to zero
        h[h == 0] = 1e-7
        self.nx = len(x)

        self.a = [iy for iy in y]
        a = self.__calculate_a(h)
        b = self.__calculate_b(h)

        # self.c = np.linalg.solve(a, b)
        a1 = [0]
        a2 = []
        a3 = []
        for row in range(len(a)):
            if row - 1 >= 0:
                a1.append(a[row][row - 1])
            a2.append(a[row][row])
            if row + 1 < len(a):
                a3.append(a[row][row + 1])
        a3.append(0)

        self.c = tdma_solve(a1, a2, a3, b)

        for i in range(self.nx - 1):
            self.d.append((self.c[i + 1] - self.c[i]) / (3.0 * h[i]))
            tb = (self.a[i + 1] - self.a[i]) / h[i] - h[i] * (self.c[i + 1] + 2.0 * self.c[i]) / 3.0
            self.b.append(tb)

        # need to add zeros to compute last indexes, because
        # b and d have 1 less elements than a and c
        self.b.append(0)
        self.d.append(0)

    def point(self, param):
        if param < self.x[0] or param > self.x[-1]:
            return None

        i = self.__search_index(param)
        dx = param - self.x[i]
        result = self.a[i] + self.b[i] * dx + self.c[i] * dx ** 2.0 + self.d[i] * dx ** 3.0
        return result

    def __search_index(self, x):
        return bisect.bisect(self.x, x) - 1

    def __calculate_a(self, h):
        result = np.zeros((self.nx, self.nx))
        result[0, 0] = 1.0
        for i in range(self.nx - 1):
            if i != (self.nx - 2):
                result[i + 1, i + 1] = 2.0 * (h[i] + h[i + 1])
            result[i + 1, i] = h[i]
            result[i, i + 1] = h[i]

        result[0, 1] = 0.0
        result[self.nx - 1, self.nx - 2] = 0.0
        result[self.nx - 1, self.nx - 1] = 1.0
        return result

    def __calculate_b(self, h):
        result = np.zeros(self.nx)
        for i in range(self.nx - 2):
            result[i + 1] = 3.0 * ((self.a[i + 2] - self.a[i + 1]) / h[i + 1] - (self.a[i + 1] - self.a[i]) / h[i])
        return result
