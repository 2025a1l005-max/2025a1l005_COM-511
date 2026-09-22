# Write a Python program to store one student data as a tuple: name, roll number, and marks. Display grade based on marks.




student = ("Divyanshu", 101, 85)
print("Student Data:")
print("Name:", student[0])
print("Roll Number:", student[1])
print("Marks:", student[2])
marks = student[2]
if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "F"
print("Grade:", grade)
