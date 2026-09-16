# White a Python program to input numbers in a list and create two separate lists for even and odd numbers.


nums = list(map(int, input("Enter numbers separated by space: ").split()))
even = [n for n in nums if n % 2 == 0]
odd  = [n for n in nums if n % 2 != 0]

print("Even numbers:", even)
print("Odd numbers:", odd)
