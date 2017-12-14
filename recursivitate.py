def sum(n):
    if n <= 0:
        return 0

    return n + sum(n-1)


def cmmdc(x, y):
    if x % y == 0:
        return y

    return cmmdc(y, x % y)


print cmmdc(10, 5)

