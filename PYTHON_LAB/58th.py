# Write a Python program to rotate a list one position to the right.


nums = list(map(int, input("Enter numbers: ").split()))
nums = [nums[-1]] + nums[:-1]
print("Rotated list:", nums)
