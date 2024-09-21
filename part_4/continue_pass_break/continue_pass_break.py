my_number = [1, 2, 3]

for i in my_number:
    if i == 2:
        print("Pass executed")
        pass
    print(i)

print()

for i in my_number:
    if i == 2:
        print("Continue executed")
        continue
    print(i)

print()

for i in my_number:
    if i == 2:
        print("Break executed")
        break
    print(i)
