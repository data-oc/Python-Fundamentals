"""
3. String
"""

string_1 = "I love Python."

# 1. Length
string_1_length = len(string_1)
print("string_1_length =", string_1_length)

# 2. Retrieve
print("I love Python." [5])     # e
print(string_1[4])              # v
print(string_1[-4])             # h
print("I love Python." [2:6])   # love
print(string_1[2:13])           # love Python
print(string_1[-12:-6])         # love P
print(string_1[7:])             # Python.
print(string_1[:-8])            # I love