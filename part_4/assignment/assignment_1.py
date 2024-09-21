import re

import main

balance = 0
is_register = False

# Name and validation
def name_input_validate (input_message, is_first_character_uppercase, warning_message):
    is_alpha = False
    while not is_alpha:
        name = input(input_message)
        if name.isalpha() and name.isascii() and len(name) > 0:
            is_alpha = True
            if not name[0].isupper() and is_first_character_uppercase is True:
                name_list = list(name)
                name_list[0] = name_list[0].upper()
                modified_name = "".join(name_list)
                name = modified_name
            else:
                continue
        else:
            print(warning_message)
    return name

def email_input_validate(input_message, warning_message):
    is_valid_email = False
    while not is_valid_email:
        email = input(input_message)
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        is_valid_email = re.match(regex, email)
        if is_valid_email and len(email) <= 320:    # 64 for local + 253 for domain + 1 for '@'
            return email
        else:
            is_valid_email = False      # prevent is_valid_email = None
            print(warning_message)

def mobile_number_input_validate(input_message, warning_message):
    is_valid_number = False
    while not is_valid_number:
        mobile_number = input(input_message)
        regex = r'^\+?[1-9]\d{1,14}$'  # Example: allows international format with '+' and up to 15 digits
        is_valid_number = re.match(regex, mobile_number)
        if is_valid_number:
            return mobile_number
        else:
            is_valid_number = False
            print(warning_message)

def float_input_validate(input_message, warning_message):
    is_valid_number = False
    while not is_valid_number:
        deposit_1 = input(input_message)
        deposit_2 = deposit_1.replace(",", "")
        regex = r'^\d*\.\d+$'
        is_valid_number = re.match(regex, deposit_2)
        if is_valid_number and float(deposit_2) > 0:
            return float(deposit_2)
        else:
            is_valid_number = False
            print(warning_message)

while not is_register:
    print("### Welcome to Bank of America ###")
    print("Press 1: Open an bank account")
    print("Press 2: Exit")
    your_choose = input("Input: ")
    print("\n", end="")

    if your_choose == "1" and is_register == False:
        first_name = name_input_validate("First name: ", True,
                                             "Please input only English alphabets.\n"
                                             "Example: Apiwat\n")
        last_name = name_input_validate("Last name: ", True,
                                             "Please input only English alphabets.\n"
                                             "Example: Tatsanakitti\n")
        email = email_input_validate("Email: ", "Invalid email address or exceeds standard length.\n")
        mobile_number = mobile_number_input_validate("Mobile number: ",
                                                     "Invalid mobile number.\n"
                                                     "Example: +66971974582\n")
        deposit = float_input_validate("Deposit: ",
                                       "Invalid number.\n"
                                       "Example: 500.0, 1,000.25, 1,000,000.0\n")
        balance += deposit
        is_register = True
    elif your_choose == "2":
        exit()
    else:
        print("\nI have to input only a number from 1 to 2.")
        input("\nPress Enter to continue.")

while is_register:
    print("\n\n### Welcome to Bank of America ###")
    print("Full name:", first_name, last_name)
    print("E-mail:", email)
    print("Mobile number:", mobile_number)
    print("Press 1: Balance")
    print("Press 2: Deposit")
    print("Press 3: Withdraw")
    print("Press 4: Exit")
    your_choose = input("Input: ")
    print("\n", end="")

    if your_choose == "1" and is_register:
        print("Balance =", balance)
        input("\nPress Enter to continue.")
    elif your_choose == "2" and is_register:
        deposit = float_input_validate("Deposit: ",
                                       "Invalid number.\n"
                                       "Example: 500.0, 1,000.25, 1,000,000.0\n")
        balance += deposit
        print("Balance =", balance)
        input("\nPress Enter to continue.")
    elif your_choose == "3" and is_register:
        print("Balance before withdrawing cash. =", balance)
        withdraw = float_input_validate("Withdraw: ",
                                        "Invalid number.\n"
                                        "Example: 500.0, 1,000.25, 1,000,000.0\n")
        if balance >= withdraw:
            balance -= withdraw
            print("Balance after withdrawing cash. =", balance)
        else:
            print("You don't have enoght money.")
        input("\nPress Enter to continue.")
    elif your_choose == "4":
        exit()
    else:
        print("You have to input only a number from 1 to 4.\n")
        input("Press Enter to continue.")