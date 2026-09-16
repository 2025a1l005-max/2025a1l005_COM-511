# Write a Python program to input marks of 10 students. Store only valid marks between 0 and 100 in a list. Skip
# invalid marks.

marks = []
for i in range(10):
    try:
        m = int(input(f"Marks {i+1}: "))
        if 0 <= m <= 100: marks.append(m)
    except: pass
print(marks)
