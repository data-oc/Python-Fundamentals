import re

text1 = "I fly to the moon."
text2 = "I run to India."

x1 = re.findall("walk|run", text1)
x2 = re.findall("walk|run", text2)

print("x1 =", x1)
print("x2 =", x2)