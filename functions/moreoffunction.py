# more of function


def power_function(number: int = 10) -> int:
    """Function with type hints"""

    return number * number


print(power_function())


def args_function(*numbers):
    return sum(numbers)


print(args_function(1, 2, 3, 4, 5, 6, 6, 7, 7))
