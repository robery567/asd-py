class Fraction:
    def __init__(self, fraction_numerator, fraction_denominator):
        self.fraction_numerator = fraction_numerator
        self.fraction_denominator = fraction_denominator
        self.__reduce_fraction()

    def __smallest_common_divisor(self, x, y):
        if x % y == 0:
            return y

        return self.__smallest_common_divisor(y, x % y)

    def __add__(self, fraction):
        if self.fraction_denominator != fraction.fraction_denominator:
            return Fraction(self.fraction_numerator * fraction.fraction_denominator
                            + fraction.fraction_numerator * self.fraction_denominator,
                            self.fraction_denominator * fraction.fraction_denominator)
        else:
            return Fraction(self.fraction_numerator + fraction.fraction_numerator, self.fraction_denominator)

    def __mul__(self, fraction):
        return Fraction(self.fraction_numerator * fraction.fraction_numerator,
                        self.fraction_denominator * fraction.fraction_denominator)

    def __sub__(self, fraction):
        if self.fraction_denominator != fraction.fraction_denominator:
            return Fraction(self.fraction_numerator * fraction.fraction_denominator
                            - fraction.fraction_numerator * self.fraction_denominator,
                            self.fraction_denominator * fraction.fraction_denominator)
        else:
            return Fraction(self.fraction_numerator - fraction.fraction_numerator, self.fraction_denominator)

    def __div__(self, fraction):
        return Fraction(self.fraction_numerator * fraction.fraction_denominator,
                        self.fraction_denominator * fraction.fraction_numerator)

    def __reduce_fraction(self):
        common_divisor = self.__smallest_common_divisor(self.fraction_numerator, self.fraction_denominator)
        self.fraction_numerator /= common_divisor
        self.fraction_denominator /= common_divisor

    def get_fraction(self):
        return [self.fraction_numerator, self.fraction_denominator]
