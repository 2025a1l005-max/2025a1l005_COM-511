# Write a python program to store all month names in a tuple. Input a month number and display the corresponding  month name.


months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")
month_number = int(input("Enter month number (1-12): "))
if 1 <= month_number <= 12:
    print("Month name:", months[month_number - 1])
else:
    print("Invalid month number! Please enter between 1 and 12.")
