import random


class Networking:
    def __init__(self):
        self.first_segment = "127"
        self.second_segment = "0"
        self.third_segment = "0"
        self.fourth_segment = "1"

    def generate_ip(self):
        self.first_segment = str(random.randint(1, 255))
        self.second_segment = str(random.randint(0, 255))
        self.third_segment = str(random.randint(0, 255))
        self.fourth_segment = str(random.randint(0, 255))

    def get_ip(self):
        return self.first_segment + "." + self.second_segment + "." + self.third_segment + "." + self.fourth_segment
