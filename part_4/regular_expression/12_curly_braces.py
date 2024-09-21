import re

text1 = "Hello"
text2 = "Helllllo"

x1 = re.findall("He.{2}o", text1)
x2 = re.findall("He.{2}o", text2)

print("x1 =", x1)
print("x2 =", x2)