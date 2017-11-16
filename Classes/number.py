class Number:
    def __init__(self, value):
        self.value = value

    def to_base2(self):
        if type(self.value) != "int":
            return 0

        base2_number = []

        for i in range(15):
            base2_number.append(self.value)
            self.value /= 2

        base2_number.append(abs(self.value))

        self.value = base2_number[::-1]

    def to_base10(self):
        if self.value[0] == 1:
            new_value = -1
        else:
            new_value = 0

        for i in range(1, 16):
            new_value *= 2
            new_value += int(self.value[i])

        self.value = new_value

    def sum_base2_values(self, x, y):
        base2_sum = []
        transport = 0

        for i in range(7, -1, -1):
            base2_sum.append((x[i] + y[i] + transport) % 2)

            if (x[i] and y[i]) or (x[i] or y[i] and transport):
                transport = 1
            else:
                transport = 0

        return base2_sum[::-1], base2_sum[7]

    def get_value(self):
        return self.value
