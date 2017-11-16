import math
v = list(range(200))
# a = input("a=")
# b = input("b=")


# def max_min(a, b):
#     min = min(a, b)
#     max = max(a, b)
#
#     return min, max
#
# m, n = max_min(a, b)
#
# print "Min: %d, Max: %d" % (m, n)


def is_prime(x):
    if x == 1:
        return 0

    for i in range(2, x):
        if x % i == 0:
            return 0

    return 1


def get_prime_factors(n):
    found_primes = 0

    for i in range(2, int(math.sqrt(n))):
            if n % i == 0 and is_prime(i):
                v[found_primes] = i
                found_primes = found_primes + 1

    return v

primes = get_prime_factors(125)

for var in primes:
    print var