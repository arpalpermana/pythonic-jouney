# is not really necessary actually

number1 = 10  # initiate variable
number2 = 12  # still
print(f"The number {number1}, has biner = {format(number1, "08b")}")  # see the biner
print(f"The number {number2}, has biner = {format(number2, "08b")}")  # see the biner

newBiner = number1 | number2  # also can use &, ^, ~ (bit logic)
print(f"number1 OR number2 in biner is: {format(newBiner, "08b")}")
