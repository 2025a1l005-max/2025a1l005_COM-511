# Write a Python program to input numbers in a list and find the second largest number.


nums = list(map(int, input("Enter numbers separated by space: ").split()))
unique_nums = list(set(nums))
if len(unique_nums) < 2:
    print("Not enough numbers to find second largest.")
else:
    unique_nums.sort(reverse=True)
    print("Second largest number is:", unique_nums[1])
