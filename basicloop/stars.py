# basic loop exercise with creating starts

counter = int(input("How much do you want? "))

print("Looping using for")
for i in range(1, counter + 1):
    print("*" * i)

print("\nLooping using while")
i = 1
while True:
    print("*" * i)
    i += 1
    if i > counter:
        break

print("\nLoops odd only")
for i in range(1, counter + 1):
    if i % 2:
        print("odd")
        continue
    print("*" * i)

print("\nLoops with space")
i = 1
while counter > 0:
    counter -= 1
    print(" " * counter, "+" * i)
    i += 1

print("\nTriangle")
counter = 8
i = 1
space = int(counter / 2)
while True:
    if i % 2:
        print(" " * space, "+" * i)
        space -= 1
        i += 1
    else:
        i += 1
        continue

    if i > counter:
        break
counter = 1
i = 8
space = int(counter / 1)
while True:
    if i % 2:
        print(" " * space, "+" * i)
        space += 1
        i -= 1
    else:
        i -= 1
        continue

    if i < counter:
        break
