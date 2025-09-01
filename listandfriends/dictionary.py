# data collection with key-value access

data_dict = {
    "one": 1,
    "two": "two",
    "three": False,
    "four": [1, 2, 3, 4, 5],
    "five": {
        "one": 123,
        "two": 100,
    },
}

# print(data_dict["five"]["one"])

for key in data_dict:  # get loop from dictionary
    print(data_dict.get(key))

for value in data_dict.values():  # this is also a loop
    print(value)

for item in data_dict.items():  # yeah yeah
    print(item)

for key, value in data_dict.items():  # this too
    print(f"key: {key}, item: {value}")

data_five = data_dict.pop("five")  # pop pop pop
print(f"data_five = {data_five}")
print(f"data_dict after pop = {data_dict} \n")

last_data_dict = data_dict.popitem()  # pop last item in dictionary
print(f"last_data_dict: {last_data_dict}")
print(f"data_dict after pop = {data_dict} \n")
