# Write a Python program to count how many times a particular element appears in a list.


nums = list(map(int, input("Enter numbers separated by space: ").split()))
x = int(input("Enter element to count: "))
print(f"{x} appears {nums.count(x)} times in the list.")
