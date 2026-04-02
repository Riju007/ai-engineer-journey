from math import sqrt


def get_list_sum(data: list[int | float]) -> float:
    total: float = 0.00
    for i in data:
        total += i
    return total


def check_input_list_is_valid(data: list[int | float]) -> tuple[int, bool]:
    """Check if the input list is valid or not."""
    all_data_valid = []
    len_data: int = len(data)
    if len_data == 0:
        raise ValueError("Input data list is empty. Please check your input")
    for i in data:
        if isinstance(i, (int, float)):
            all_data_valid.append(True)
        else:
            all_data_valid.append(False)
    is_valid_data: bool = all(all_data_valid)
    return (len_data, is_valid_data)


def mean(data: list[int | float], len_data) -> float:
    """Get the mean(avg) value from a list."""
    total: float = get_list_sum(data)
    mean: float = total / len_data
    return mean


def squared_differences(data: list[float | int], len_data) -> list[float]:
    """Get the squared difference in a list"""
    output_list: list[float] = []
    mean_value: float = mean(data, len_data)
    for i in data:
        squared_diff: float = (i - mean_value) ** 2
        output_list.append(squared_diff)
    return output_list


def standard_deviation(data: list[float | int]) -> float:
    """Get the standard deviation."""
    len_data, is_valid_data = check_input_list_is_valid(data)
    if is_valid_data:
        squared_difference_list = squared_differences(data, len_data)
        print(f"Squared diff list: {squared_difference_list}")
        variance = get_list_sum(squared_difference_list) / len_data
        print(f"Variance is: {variance}")
        std = sqrt(variance)
        return std
    else:
        raise ValueError("Invalid input list")


if __name__ == "__main__":
    # input_list_01 = [i for i in range(1, 10)]
    # mean_value_01 = mean(input_data_list=input_list_01)
    # print(f"Mean value 01 is: {mean_value_01}")
    # squared_diff = squared_differences(input_list_01)
    # print(f"Sqrt list: {squared_diff}")
    input_list_01 = [2, 4, 6, 8]
    # input_list_01 = []
    # input_list_01 = ["a", "b", 1, 5, 7]
    std = standard_deviation(input_list_01)
    print(f"Standard Deviation is: {std:.2f}")
