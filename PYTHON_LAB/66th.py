# Write a Python program to check whether a given value is present in a tuple. If present, display its position




numbers = (10, 20, 30, 40, 20, 50)
print("Tuple:", numbers)
value = int(input("Enter a value to search: "))
if value in numbers:
    print(f"The value {value} is present in the tuple.")
    positions = [i for i, v in enumerate(numbers) if v == value]
    print("Positions:", positions)
else:
    print(f"The value {value} is not present in the tuple.")
