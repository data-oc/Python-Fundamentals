input_number = int(input("Enter number: "))

for i in range(input_number+1):
    for j in range(i):
        print(i, end=" ")
    print()

"""
Enter number: 4

1
2 2
3 3 3
4 4 4 4
"""