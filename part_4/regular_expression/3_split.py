import re

text = "The rain in Spain"

x1 = re.split("\\s", text)

print("x1 =", x1)

x2 = re.split("\\s", text, 2)

print("x2 =", x2)
