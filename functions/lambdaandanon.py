# lambda and anonymous function

math_power = lambda number, power: number**power
print(math_power(10, 3))

list_data = ["Chicken", "Fish", "Cow"]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_data)

filtered_list_data = list(filter(lambda number: number % 2 == 1, numbers))
print(filtered_list_data)
