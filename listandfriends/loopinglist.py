# looping with list

numbers = [2, 5, 10, 3, 7]

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

print("\n")
[print(i) for i in numbers]

for index, data in enumerate(sorted(numbers)):
    print(f"for index {index}, the data is {data}")
