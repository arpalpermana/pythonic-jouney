# global and local scope

number = 0


def change_number(new_number):
    global number  # need global keyword to access global variable in function
    number = new_number


print(f"before = {number}")
change_number(20)
print(f"after = {number}")
