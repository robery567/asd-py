class Algorithm:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def run_algorithm(self, number):
        call_method = getattr(self, "__algorithm" + number)

        return call_method()

    def __algorithm1(self):
        if self.a < self.b:
            aux = self.a
            self.a = self.b
            self.b = aux
        c = 0
        d = self.a

        while d > self.b:
            c += 1
            d -= self.b

        return c, d

    def __algorithm2(self):
        i = 1
        x = 0

        while i <= self.n:
            i *= 2
            x += 1

        return x
