# Write a Python program to store multiple student records as a list of tuples. Each tuple should contain name, roll number, and marks. Display students who scored above 75.




students = [
    ("div", 101, 85),
    ("divya", 102, 72),
    ("divyanshu", 103, 90),
    ("divyansh", 104, 65),
    ("divu", 105, 78)
]
for name, roll, marks in students:
    if marks > 75:
        print(name, roll, marks)
