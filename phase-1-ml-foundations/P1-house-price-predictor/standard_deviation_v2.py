from math import sqrt


class RunningState(object):

    def __init__(self):
        self.count = 0
        self.sum_x = 0
        self.sum_x_2 = 0

    def add(self, num):
        self.count += 1
        self.sum_x += num
        self.sum_x_2 += num**2

    def get_std(self):
        if self.count == 0:
            raise ValueError("There is no value")
        mean = self.sum_x / self.count
        mean_square = mean**2
        variance = (self.sum_x_2 / self.count) - mean_square
        variance = max(variance, 0.0)
        sd = sqrt(variance)
        return sd


if __name__ == "__main__":
    obj = RunningState()
    # obj.get_std()
    obj.add(2)
    obj.add(4)
    obj.add(6)
    obj.add(8)
    sd = obj.get_std()
    print(f"SD is: {sd}")
