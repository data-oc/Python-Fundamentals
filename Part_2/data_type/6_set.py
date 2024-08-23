"""
6. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
"""

set_1 = {"Toon", "Toon", 11, -22, 123.45, True}
set_2 = {"Rolls-Royce", "Aston Matin", "Ferrari", "BMW"}
set_3 = {"Bugatti", "Ferrari", "Lamborghini", "BMW"}
set_4 = {"BMW", "Ferrari"}

set_union = set_1.union(set_2, set_3)

set_intersection = set_2.intersection(set_3)

set_defference = set_2.difference(set_3)

set_symmetric_difference = set_2.symmetric_difference(set_3)

set_disjoint_1 = set_2.isdisjoint(set_3)

set_disjoint_2 = set_3.isdisjoint(set_2)

set_disjoint_3 = set_1.isdisjoint(set_2)

set_issubset_1 = set_4.issubset(set_3)

set_issubset_2 = set_3.issubset(set_4)

set_issuperset_1 = set_4.issuperset(set_3)

set_issuperset_2 = set_3.issuperset(set_4)

# Retrieve
set_retrieve_1 = "Lamborghini" in set_union
set_retrieve_2 = "Bugatti" not in set_union

# Add / Insert
set_4.add("McLaren")

# Update
set_4_list = list(set_4)
set_4_list[1] = "Audi"
set_4 = set(set_4_list)

# Delete
set_1.discard(True)
set_1.discard(-22)      # discard() will not raise an error.

'''
set_1.remove(11)
set_1.remove("Toon")    # remove() will raise an error.
set_1.remove(11)
'''

set_1.pop()

# Clear
set_1.clear()


