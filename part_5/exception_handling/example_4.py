try:
    number_dict = {
        1: "one",
        2: "two",
        3: "three"
    }

    number_list = [1, 2, 3]

    print(number_dict[2])
    print(number_list[2])

except KeyError:
    print("Your key is invalid.")
except IndexError:
    print("Your index is invalid.")
finally:
    print("Done")

"""
else:
    print("Done")
"""

