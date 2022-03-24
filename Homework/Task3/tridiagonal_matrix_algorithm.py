def run_through(a, b, c, d):
    n = len(d)

    c[0] /= b[0]
    d[0] /= b[0]

    for i in range(1, n):
        ptemp = b[i] - (a[i] * c[i - 1])
        c[i] /= ptemp
        d[i] = (d[i] - a[i] * d[i - 1]) / ptemp


def substitution(c, d):
    n = len(d)

    x = [0 for i in range(n)]
    x[-1] = d[-1]
    for i in range(-2, -n - 1, -1):
        x[i] = d[i] - c[i] * x[i + 1]
    return x


if __name__ == "__main__":
    matrix = [
        [1, 8, 0, 0, 0], [1],
        [1, 4, 2, 0, 0], [5],
        [0, 3, 2, 2, 0], [3],
        [0, 0, 6, 3, 1], [4],
        [0, 0, 0, 6, 2], [7]
    ]
    a = [0, 1, 3, 6, 6]
    b = [1, 4, 2, 3, 2]
    c = [8, 2, 2, 1, 0]
    d = [1, 5, 3, 4, 7]

    run_through(a, b, c, d)
    x = substitution(c, d)
    print(x)
