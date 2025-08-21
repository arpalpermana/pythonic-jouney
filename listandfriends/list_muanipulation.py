# list manipulation

list_list = [1, True, "Three"]

print(list_list[2])

list_list.insert(2, 2)
print(list_list)

list_list.append(4)
print(list_list)

list_list.extend(["Five", 6, "Seven"])
print(list_list)

list_list[1] = "True"
list_list.remove("True")
print(list_list)

list_list.pop()
print(list_list)
