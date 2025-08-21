# control flow like an avatar

for i in range(5):

    if i == 2:
        print(f"i = {i}")
        continue

    if i == 3:
        pass

    if i == 4:
        break

    print(i)
