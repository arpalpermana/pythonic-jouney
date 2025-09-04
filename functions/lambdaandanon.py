# lambda and anonymous function

math_power = lambda number, power: number**power
print(math_power(10, 3))

list_data = ["Chicken", "Fish", "Cow"]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_data)

filtered_list_data = list(filter(lambda number: number % 2 == 1, numbers))
print(filtered_list_data)


def math_pow(pow):
    return lambda number: number**pow


power_by_2 = math_pow(2)
print(f"5 power 2 is {power_by_2(5)}")
print(f"3 power 2 is {math_pow(2)(3)}")
