# basic function in python


def say_hello(name):
    print(f"Hello {name}")


input_name = str(input("What is your name? "))
say_hello(input_name)


def simple_math(operator, number1, number2=1):
    operations = {
        "+": number1 + number2,
        "-": number1 - number2,
        "/": number1 / number2,
        "*": number1 * number2,
    }

    return "".join(
        f"{number1} {op} {number2} = {result} \n" for op, result in operations.items()
    )


print(simple_math("+", 9))
print(simple_math("-", number2=10, number1=11))


def first_three(list_input):
    number1 = list_input[0]
    number2 = list_input[1]
    number3 = list_input[2]

    return number1, number2, number3


numbers = [1, 2, 3, 4, 5]
a, b, c = first_three(numbers)
print(a, b, c)
