import time
import math


def g(x):
    return math.exp(x) - 2


def function_zero(f, a, b):
    """Returns zero of f between a and b. Assumes that f(a) < 0, f(b) > 0."""
    """ ищет нуль функции f на отрезке [a,b], когда f(a) < 0, f(b) > 0"""
    while abs(b - a) > 1e-6:
        c = (a + b) / 2
        fc = f(c)
        if fc > 0:
            b = c
        else:
            a = c
    return (a + b) / 2


"""интеграл от a до b"""
def integrate(f, a, b):
    res = 0
    t = a
    ft = f(t)
    dt = 1e-6
    while t + dt < b:
        ftdt = f(t + dt)
        res += dt * (ft + ftdt) / 2
        t += dt
        ft = ftdt
    res += (b - t) * (ft + f(b)) / 2
    return res


def derivative(f, a):
    da = 1e-6
    # return (f(a + da) - f(a - da)) / 2 / da
    return (f(a + da) - f(a)) / da


start_time = time.time()

print(integrate(g, 0, 1))
print(math.exp(1) - 3)

print(f"Elapsed time: {time.time() - start_time:.4f} seconds")
