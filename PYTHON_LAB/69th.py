# 1. Write a Python program to input a student's marks in n consecutive tests and store them in a list. Find the longest consecutive sequence in which each mark is strictly greater than the previous mark.
# Display the sequence, its length, and its starting and ending test numbers as a tuple. If multiple sequences have the same maximum length, display the first one.

#Marks: [55, 60, 68, 62, 65, 70, 78, 74)
#Longest improving sequence: [62, 65, 70, 78]
#Number of tests: 4
#Test range: (4, 7)
#Conditions:
#Accept at least one test.
#Equal marks break the improving sequence.
#Test numbers begin at 1.
#Do not sort the list because the original test order matters.




marks = list(map(int, input("Enter marks: ").split()))
start = best_start = 0
length = best_len = 1

for i in range(1, len(marks)):
    if marks[i] > marks[i-1]:
        length += 1
        if length > best_len:
            best_len, best_start = length, start
    else:
        start, length = i, 1

seq = marks[best_start:best_start+best_len]
print("Longest improving sequence:", seq)
print("Number of tests:", best_len)
print("Test range:", (best_start+1, best_start+best_len))
