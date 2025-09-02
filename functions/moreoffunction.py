# more of function


def power_function(number: int = 10) -> int:
    """Function with type hints"""

    return number * number


print(power_function())


def args_function(*numbers):
    """Change multiple arguments to tuple"""
    return sum(numbers)


print(args_function(1, 2, 3, 4, 5, 6, 6, 7, 7))


def kwargs_function(**numbers):
    """Change multiple arguments to dictionary"""
    return f"number 1 = {numbers['number1']}, number2 = {numbers['number2']}"


print(kwargs_function(number1=20, number2=10))


def math_operation(*numbers, **option):
    result = 0
    if option["operator"] == "+":
        for number in numbers:
            result += number
    elif option["operator"] == "*":
        result = 1
        for number in numbers:
            result *= number
    else:
        return "Error: operator not found."

    return result


print(math_operation(1, 2, 3, operator="+"))
print(math_operation(1, 2, operator="*"))
