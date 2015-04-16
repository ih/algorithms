class TempTracker(object):
    def __init__(self):
        self.max = None
        self.min = None
        self.count = 0
        self.sum = 0
        self.temperature_counts = {}
        self.mode = None
        self.mode_count = None

    def insert(self, temperature):
        self.__set_max(temperature)
        self.__set_min(temperature)
        self.__set_mean(temperature)
        self.__set_mode(temperature)

    def __set_max(self, temperature):
        if self.max is None or self.max < temperature:
            self.max = temperature

    def __set_min(self, temperature):
        if self.min is None or self.max > temperature:
            self.min = temperature

    def __set_mean(self, temperature):
        self.count += 1
        self.sum += temperature

    def __set_mode(self, temperature):
        if temperature in self.temperature_counts:
            self.temperature_counts[temperature] += 1
        else:
            self.temperature_counts[temperature] = 1

        if (self.mode is None or
                self.mode_count < self.temperature_counts[temperature]):
            self.mode = temperature
            self.mode_count = self.temperature_counts[temperature]

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_mean(self):
        return self.sum/(self.count*1.0)

    def get_mode(self):
        return self.mode

temps = [1, 10, 2, 3, 3, 0]
t = TempTracker()
[t.insert(temp) for temp in temps]
print t.get_max()
print t.get_min()
print t.get_mean()
print t.get_mode()
