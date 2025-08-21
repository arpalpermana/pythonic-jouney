# basic use of list

first_list = [1, "True", 3, True, 5]
second_list = list(range(0, 10))

print(f"The list: {first_list}")
print(f"This is also a list: {second_list}")
print(f"You can make it like: {[i for i in range(0,5)]}")
print(f"What's the oods: {[i for i in range(1,10) if i==1 or i%2==1]}")
