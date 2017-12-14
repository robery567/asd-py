class Sorting:
    def __init__(self, input_list):
        self.input_list = input_list
        self.nrc = 0
        self.nrm = 0

    def insert(self):
        for i in range(len(self.input_list)):
            aux = self.input_list[i]
            self.nrm += 1
            j = i - 1

            while j >= 0 and aux < self.input_list[j]:
                self.nrc += 1
                self.input_list[j+1] = self.input_list[j]
                self.nrm += 1
                j -= 1

            self.nrc += 1
            self.input_list[j+1] = aux
            self.nrm += 1

    def get_list(self):
        return self.input_list

    def get_comparations_count(self):
        return self.nrc

    def get_moves_count(self):
        return self.nrm

    def bubble(self):
        m = len(self.input_list)

        t = 0
        for i in range(m - 1):
            self.nrc += 1

            if self.input_list[i] > self.input_list[i + 1]:
                # aux = self.input_list[i]
                # self.input_list[i] = self.input_list[i+1]
                # self.input_list[i+1] = aux
                self.input_list[i], self.input_list[i + 1] = self.input_list[i + 1], self.input_list[i]
                self.nrm += 3
                t = i

        m = t+1

        while t >= 1:
            for i in range(m-1):
                self.nrc += 1

                if self.input_list[i] > self.input_list[i+1]:
                    # aux = self.input_list[i]
                    # self.input_list[i] = self.input_list[i+1]
                    # self.input_list[i+1] = aux
                    self.input_list[i], self.input_list[i+1] = self.input_list[i+1], self.input_list[i]
                    self.nrm += 3
                    t = i
            m = t+1

    def selection(self):
        for i in range(len(self.input_list)-1):
            k = i

            for j in range(i+1, len(self.input_list)):
                self.nrc += 1

                if self.input_list[k] > self.input_list[j]:
                    k = j

                if k != i:
                    self.input_list[k], self.input_list[i] = self.input_list[i], self.input_list[k]
                    self.nrm += 3
