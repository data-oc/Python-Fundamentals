import re

text1 = "Hello"
text2 = "Helllllo"
text3 = "Heo"
text4 = "Helo"

# ? ไม่มีการ Match กับอักขระเลย หรือ Match กับอักขระแค่ 1 ตัวเท่านั้น

x1 = re.findall("He.?o", text1)
x2 = re.findall("He.?o", text2)
x3 = re.findall("He.?o", text3)
x4 = re.findall("He.?o", text4)

print("x1 =", x1)
print("x2 =", x2)
print("x3 =", x3)
print("x4 =", x4)