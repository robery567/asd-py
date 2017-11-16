def is_asc(l):
    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            return 0

    return 1


print is_asc([1, 2, 3, 4, 5])


def max_min(l):
    max = 0
    min = l[0]

    for el in l:
        if el > max:
            max = el

        if el < max:
            min = el

    return min, max

data_max_min = max_min([1, 2, 3, 4, 5])
print "Min: ", data_max_min[0], "\n", "Max: ", data_max_min[1]


def par_impar(l):
    sp = 0
    pi = 1

    for i in range(len(l)):
        if i % 2 == 0:
            sp += l[i]
        else:
            pi *= l[i]

    return sp, pi

print par_impar([1, 2, 3, 4, 5])


def generate_random(seed, n):
    v = list(range(200))
    a = 1103515245
    b = 12345
    c = 1

    for i in range(1, 31):
        c *= 2

    x = seed
    k = 1

    for i in range(1, n):
        x = (a * x + b) % c
        k += 1
        v[k] = x % 6 + 1

    return v


def frequency(l):
    f = list(range(7))

    for i in range(0, len(l)):
        f[l[i]] += 1

    for i in range(1, 7):
        f[i] = f[i] / len(l)

    return f
