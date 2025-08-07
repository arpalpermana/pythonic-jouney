# let's make some basic calculator

print(16 * "=")
print("Basic Calculator")
print(16 * "=")

number1 = float(input("Input first number : "))
operator = input("Input the operator : ")
number2 = float(input("Input first number : "))

if operator == "+":
    result = number1 + number2
    print(f"The result is: {result}")
elif operator == "-":
    result = number1 - number2
    print(f"The result is: {result}")
elif operator == "*" or operator == "x":
    result = number1 * number2
    print(f"The result is: {result}")
elif operator == "/":
    result = number1 / number2
    print(f"The result is: {result}")
else:
    print("Operator not valid")
