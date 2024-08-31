student_score = float(input("Enter your score: "))

if 80.0 <= student_score <= 100:
    print("Grade = A")
elif 75.0 <= student_score <= 79.0:
    print("Grade = B+")
elif 70.0 <= student_score <= 74.0:
    print("Grade = B")
elif 65.0 <= student_score <= 69.0:
    print("Grade = C+")
elif 60.0 <= student_score <= 64.0:
    print("Grade = C")
elif 55.0 <= student_score <= 59.0:
    print("Grade = D+")
elif 50.0 <= student_score <= 54.0:
    print("Grade = D")
elif 50.0 > student_score >= 0:
    print("Grade = F")
else:
    print("Your score is invalid.")

"""
A   --> 80 - 100
B+  --> 75 - 79
B   --> 70 - 74
C+  --> 65 - 69
C   --> 60 - 64
D+  --> 55 - 59
D   --> 50 - 54
F   --> < 50
"""