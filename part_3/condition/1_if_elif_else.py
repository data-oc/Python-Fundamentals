print("Welcome to Toon Coffee Machine")
print("Press 1: Americano")
print("Press 2: Capuccino")
print("Press 3: Mocha")
print("Press 4: Latte")
print("Press 5: Espresso")

your_choose = input("Enter number: ")

if your_choose == "1":
    print("This is your Americano.")
elif your_choose == "2":
    print("This is your Capuccino.")
elif your_choose == "3":
    print("This is your Mocha.")
elif your_choose == "4":
    print("This is your Latte.")
elif your_choose == "5":
    print("This is your Espresso.")
else:
    print("Your number is invalid.")