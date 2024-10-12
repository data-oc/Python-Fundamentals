try:
    number_1 = int(input("(1) Input integer number: "))
    number_2 = int(input("(2) Input integer number: "))
    print(number_1/number_2)
except ValueError:
    print("You did not input the integer number.")
except ZeroDivisionError:
    print("It cannot find the result.")