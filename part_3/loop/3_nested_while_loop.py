input_number = int(input("Enter number: "))
# input_number = 2
i = 1
j = 1
while i <= input_number:
    print(">> i =", i)
    j = 1
    while j <= input_number:
        print("j =", j)
        j += 1
    i += 1

"""
Enter number: 2

>> i = 1
j = 1
j = 2
>> i = 2
j = 1
j = 2
"""