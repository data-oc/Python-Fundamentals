"""
5. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
"""

tuple_1 = ("Toon", "Toon", 11, -22, 123.45, True)
tuple_1 = ("orange", "avocado")
tuple_2 = ("banana", "cherry", "strawberry")

tuple_3 = tuple_1 + tuple_2

# Count
tuple_3_length = len(tuple_3)

# Copy
tuple_3_copy = tuple_3

# Retrieve
tuple_3_index_2 = tuple_3[2]

# Add / Insert 1
tuple_3 = tuple_3 + ("grape",)

# Add / Insert 2
tuple_3_list = list(tuple_3)
tuple_3_list.insert(1, "cherry")
tuple_3 = tuple(tuple_3_list)

# Update
tuple_3_list = list(tuple_3)
tuple_3_list[3] = "mango"
tuple_3 = tuple(tuple_3_list)

# Multiply
tuple_3_multiply = tuple_3 * 2

# Delete
tuple_3_list = list(tuple_3)
tuple_3_list.remove("orange")
del tuple_3_list[0]
tuple_3 = tuple(tuple_3_list)

# Unpack
(green, yellow, *red, purple) = tuple_3