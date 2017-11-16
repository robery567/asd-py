from fraction import Fraction
from math import sqrt


class Polynomial:
    def __init__(self, coefficients, x):
        self.coefficients = coefficients
        self.x = x

    def get_value(self):
        value = Fraction(self.coefficients[0], 1)
        coefficients = iter(self.coefficients)
        next(coefficients)

        for coefficient in coefficients:
            value *= self.x
            value += Fraction(coefficient, 1)

        return value

    def get_roots(self):
        roots_list = []

        c0 = self.coefficients[len(self.coefficients)-1]
        c0_divisors = []

        for i in range(1, int(sqrt(abs(c0))) + 2):
            if c0 % i == 0:
                c0_divisors.append(i)

        cn = self.coefficients[0]
        cn_divisors = []

        for i in range(1, int(sqrt(abs(cn))) + 2):
            if cn % i == 0:
                cn_divisors.append(i)

        for numerator in c0_divisors:
            for denominator in cn_divisors:
                self.x = Fraction(numerator, denominator)

                if self.get_value().fraction_numerator == 0:
                    roots_list.append(Fraction(numerator, denominator))

        if not roots_list:
            return 0

        return roots_list
