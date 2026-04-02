from math import sqrt


class RunningState(object):
    data = []

    def add(self, num):
        self.data.append(num)
        return None

    def get_std(self):
        data_list = self.data
        len_data = len(data_list)
        list_sum = sum(data_list)
        mean = list_sum / len_data
        print(f"mean is: {mean}")
        list_sum_square = sum(list(map(lambda x: x ** 2, data_list)))
        mean_square = mean ** 2
        print(mean_square)
        print(list_sum_square)
        variance = (list_sum_square / len_data) - (mean ** 2)
        print(variance)
        sd = sqrt(variance)
        return sd


if __name__ == "__main__":
    obj = RunningState()
    obj.add(2)
    obj.add(4)
    obj.add(6)
    # obj.add(8)
    print(f"data list is :{obj.data}")
    sd = obj.get_std()
    print(f"SD is: {sd}")
