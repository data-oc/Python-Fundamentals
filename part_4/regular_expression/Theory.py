"""
Python Regular Expression (RegEx)
1. RegEx Functions
    1.1 findall
    1.2 search
    1.3 split
    1.4 sub
2. Metacharacters
[] = Match ในกลุ่มของอักขระที่เรากำหนด
เช่น [a - c]

. = Match ทุกอักขระ
เช่น he..o

^ = Match คำที่ขึ้นต้นด้วยอักขระที่เรากำหนด
เช่น ^hello

$ = Match คำที่ลงท้ายด้วยอักขระที่เรากำหนด
เช่น toon$

* = ไม่มีการ Match กับอักขระเลย หรือ Match กับอักขระมากกว่า 1 ตัวขึ้นไป
เช่น he.*o
ตัวอย่างข้อความ
helllllllo
heo

+ = ต้อง Match กับอักขระตั้งแต่ 1 ตัวขึ้นไป
เช่น he.+o
ตัวอย่างข้อความ
helllllo
heo

? = ไม่มีการ Match กับอักขระเลย หรือ Match กับอักขระ 1 ตัว
เช่น he.?o
ตัวอย่างข้อความ
helllllo
heo

{} = ต้อง Match กับจำนวนอักขระที่เรากำหนดไว้
เช่น he.{2}o
ตัวอย่างข้อความ
helllllo
heo

| = ต้อง Match กับอักขระอันใดอันหนึ่งที่เรากำหนดไว้
เช่น run|walk
ตัวอย่างข้อความ
I walk to the moon

3. Special Sequences
4. Sets
"""