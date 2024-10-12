"""
If we use "raise Exception," we can still use "try" and "except." 

Example:
try:
    # Some code that may raise an exception
    raise Exception("An error occurred")
except Exception as e:
    print(f"Caught an exception: {e}")
"""

my_input = int(input("Your input: "))

if my_input < 1 or my_input > 100:
    raise Exception("Your input must has number from 1 to 100.")
else:
    print(my_input)
