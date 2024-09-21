import re

text = "The rain in Spain"

x1 = re.findall("ai", text)

print("x1 =", x1)

x2 = re.findall("England", text)

print("x2 =", x2)