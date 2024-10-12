# If we use "raise exception" we cannot use "try" and "except".

my_input = int(input("Your input: "))

if my_input < 1 or my_input > 100:
    raise Exception("Your input must has number from 1 to 100.")
else:
    print(my_input)

