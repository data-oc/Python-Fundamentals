"""
4. List is a collection which is ordered and changeable. Allows duplicate members.
"""

list_1 = ["Tony", "Steve"]
list_2 = ["Natasha", "Strange", "Carol"]

list_3 = list_1 + list_2

# Copy
list_4 = list_3.copy()

# Retrieve
list_3_index_0 = list_3[0]
list_3_index_3 = list_3[3]
list_3_index_minus_1 = list_3[-1]

# Add / Insert
list_3.append("Wanda")
list_3.insert(1, "Brunce")

# Update
list_3[0:2] = ["Peter", "James"]

# Delete
# list_3.remove("Steve")
# del list_3[3]
# list_3_pop = list_3.pop(4)

# Clear
# list_3.clear()

# Multiply
list_3_multiply = list_3 * 2