#Write a python program to input marks of n students in a list. Display highest
# marks, Lowest marks, average marks and number of students who passed.


n = int(input("Enter number of students: "))
marks = [int(input(f"Marks of student {i+1}: ")) for i in range(n)]

print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", sum(marks)/n)
print("Passed:", sum(m >= 40 for m in marks))