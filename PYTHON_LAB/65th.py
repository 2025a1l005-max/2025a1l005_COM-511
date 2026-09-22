#  Write a Python program to store repeated values in a tuple and count how many times a given value appears.



numbers = (1, 2, 3, 2, 4, 2, 5, 3, 2, 6)
print("Tuple:", numbers)
value = int(input("Enter a value to count: "))
count = numbers.count(value)
print(f"The value {value} appears {count} times in the tuple.")
