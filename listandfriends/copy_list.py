# how how to duplicate list

list_a = [1, 2, 3, 4, 5]

print(list_a)

list_b = list_a  # this is not copying the list, the ID will refers to the same list
print(list_b)

list_b.sort(reverse=True)
print(f"list a: {list_a}")
print(f"list b: {list_b}")

list_c = list_a.copy()  # this is how you copy a list
list_c.sort()
print(f"list a: {list_a}")
print(f"list b: {list_b}")
print(f"list c: {list_c}")
