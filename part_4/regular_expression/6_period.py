import re

text1 = "Hexyo"
text2 = "Helllllo"
text3 = "Helo"

x1 = re.findall("He..o", text1)
x2 = re.findall("He.....o", text2)
x3 = re.findall("He..o", text3)

print("x1 =", x1)
print("x2 =", x2)
print("x3 =", x3)
