def f(list):
    f = 0
    for i in range(0, len(list) - 1):
        f += (1 - list[i]) ** 2 + 100 * (list[i + 1] - list[i] ** 2) ** 2
    return f
    # return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


def grad(list):
    f1 = [-2 * (1 - list[0]) - 400 * (list[1] - list[0] ** 2) * list[0]]
    for i in range(1, len(list) - 1):
        f1[i] += [
            -2 * (1 - list[i]) - 400 * (list[i + 1] - list[i] ** 2) * list[i] + 200 * (list[i] - list[i - 1] ** 2)]
    f1 += [200 * (list[len(list) - 1] - list[len(list) - 2] ** 2)]
    return f1


def function(f, f1, x0, type):
    e = 0.001
    L = [0.01, 0.01]
    x1 = [i for i in x0]
    x2 = [(x1[i] - L[i] * f1(x1[i])) for i in range(len(x1))]
    while abs([(x2[i] - x1[i]) for i in range(len(x1))]) > e:
        x1 = [i for i in x2]
        x2 = [(x1[i] - L[i] * f1(x1[i])) for i in range(len(x1))]
        if type == 2:
            L /= 2

    return f(x2), x2


x0 = [2, 2]
print(function(f, grad, x0, 1))
