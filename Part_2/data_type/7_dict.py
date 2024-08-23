"""
7. Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

banknote_dict = {
    100: "One hundred bahts",
    500: "Five hundred bahts",
    1000: "One thousand bahts"
}

# Copy
banknote_dict_copy = banknote_dict

# Retrieve
banknote_dict_500 = banknote_dict.get(500)

banknote_dict_keys = banknote_dict.keys()

banknote_dict_values = banknote_dict.values()

banknote_dict_items = banknote_dict.items()

# Add / Insert
banknote_dict[20] = "Twenty bahts"
banknote_dict[50] = "Fifty bahts"

# Update
banknote_dict[500] = "Five hundred dollars"
banknote_dict.update({100: "One hundred dollars"})

# Delete
banknote_dict_pop = banknote_dict.pop(1000)

banknote_dict_popitem_1 = banknote_dict.popitem()
banknote_dict_popitem_2 = banknote_dict.popitem()

del banknote_dict[100]

# Clear
banknote_dict.clear()

# Nested dictionary
family_dict = {
    "father": {
        "nickname": "Toon",
        "birth_year": 1978
    },
    "mother": {
        "nickname": "Emily",
        "birth_year": 1977
    },
    "child_1": {
        "nickname": "Ava",
        "birth_year": 2015
    },
    "child_2": {
        "nickname": "Grace",
        "birth_year": 2020
    }
}

# Copy
family_dict_copy = family_dict

# Retrieve
family_dict_child_1_nickname = family_dict["child_1"]["nickname"]

# Add / Insert
family_dict["mother"]["salary"] = 100000

# Update
family_dict["child_2"]["nickname"] = "Kate"

# Delete
del family_dict["child_1"]["birth_year"]

# Clear
family_dict.clear()