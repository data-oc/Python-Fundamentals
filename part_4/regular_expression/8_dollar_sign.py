import re

text = "Hello, I'm Toon."

x1 = re.findall("Toon.$", text)

print("x1 =", x1)
