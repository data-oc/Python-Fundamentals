import re

text1 = "Hello"
text2 = "Helllllo"
text3 = "Heo"

# + ต้อง Match กับอักขระตั้งแต่ 1 ตัวขึ้นไป

x1 = re.findall("He.+o", text1)
x2 = re.findall("He.+o", text2)
x3 = re.findall("He.+o", text3)

print("x1 =", x1)
print("x2 =", x2)
print("x3 =", x3)