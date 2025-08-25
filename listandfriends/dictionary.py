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

print(data_dict["five"]["one"])
