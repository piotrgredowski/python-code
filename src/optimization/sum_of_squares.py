import timeit


def sum_of_squares_v1(numbers):
    result = 0
    for number in numbers:
        result += number**2
    return result


def sum_of_squares_v2(numbers):
    result = 0
    for number in numbers:
        # Premature optimization by using bitwise operations (unnecessary here)
        result += (number << 1) * (number >> 1) + number
    return result


# def sum_of_squares_v3(numbers):
#     import numpy as np
#     # Using a more efficient built-in function for large datasets
#     return np.sum(np.square(numbers))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(sum_of_squares_v1.__name__, sum_of_squares_v1(numbers))  # Output: 55
    print(sum_of_squares_v2.__name__, sum_of_squares_v2(numbers))  # Output: 55
    # print(sum_of_squares_v3.__name__, sum_of_squares_v3(numbers))  # Output: 55

    print(
        sum_of_squares_v1.__name__,
        timeit.timeit(lambda: sum_of_squares_v1(numbers * 1000), number=1_000),
    )
    print(
        sum_of_squares_v2.__name__,
        timeit.timeit(lambda: sum_of_squares_v2(numbers * 1000), number=1_000),
    )
    # print(sum_of_squares_v3.__name__, timeit.timeit(lambda: sum_of_squares_v3(numbers * 1000), number=1_000))  # noqa: E501
