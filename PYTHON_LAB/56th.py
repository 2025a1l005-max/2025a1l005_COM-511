# Write a Python program to input a list of numbers and create a new list containing only unique elements.


nums = list(map(int, input("Enter numbers: ").split()))
unique = list(set(nums))
print("Unique elements:", unique)
