import math


def aprox_sum(x, eps):
    x1 = x
    x2 = (-x ** 3) / 6.
    sum = x1 + x2

    n = 2

    while math.fabs(x1 - x2) > eps:
        n += 1
        x1 = x2
        x2 = (((-1)**n) * x**(2*n + 1)) / math.factorial(2*n + 1)
        sum += x2

    return sum


def aprox_sum2(eps, x):
    s0 = x
    s1 = s0 + (-x ** 3) / 6.
    n = 2

    while math.fabs(s0 - s1) > eps:
        n += 1
        s0 = s1
        s1 = s0 + (((-1)**n) * x**(2*n + 1)) / math.factorial(2*n + 1)

    return s1

print aprox_sum2(0.1, 130)
print math.sin(130)
