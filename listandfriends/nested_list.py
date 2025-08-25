# list but nested

data_0 = [0, 1]
data_1 = [2, 3]

data = [data_0, data_1, 4, 5, 6]
print(data)
print(data[0][1])

participant_1 = ["John", 25, "Male"]
participant_2 = ["Khan", 20, "Male"]
participant_3 = ["Denise", 22, "Female"]
list_of_participant = [participant_1, participant_2, participant_3]

for participant in list_of_participant:
    print(f"name \t: {participant[0]}")
    print(f"age \t: {participant[1]}")
    print(f"gender \t: {participant[2]} \n")

from copy import deepcopy

data_copy = deepcopy(
    data
)  # we need to use deepcopy to copy nested list cause the list item would have same address if we only use copy
