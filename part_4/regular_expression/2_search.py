import re

text = "The rain in Spain"

x1 = re.search("\\s", text)

print("Space =", x1.start())

x2 = re.search("Spain", text)
print("x2 =", x2)