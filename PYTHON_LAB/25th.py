number =  input("Enter 10 digit number:")
first_6 = number[:5]

print(first_6.replace(first_6,'******')+number[-4:])
