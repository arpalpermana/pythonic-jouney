# operation can be used on python

numbers = [1, 3, 2, 3, 3, 2, 4, 4, 42, 3, 5, 2]

print(f"How much is number 4? {numbers.count(4)}")

print(f"Where is number 3? {numbers.index(3)}")

numbers.sort(reverse=True)
print(f"I said reverse, {numbers}")
