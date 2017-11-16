import math


def aprox_limit(eps):
    x1 = 2
    x2 = (1 + 1. / 2)**2
    n = 2

    while math.fabs(x2 - x1) > eps:
        x1 = x2
        n += 1
        x2 = (1 + 1. / n) ** n

    return x2


print "Suma este", aprox_limit(0.1)
print "Suma este", aprox_limit(0.001)
print "Suma este", aprox_limit(0.0000000001)
print math.exp(1)
