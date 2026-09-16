#simulate a digital lock

pin = input("Please Enter 4 Digit Pin: ")

if(len(pin)==4 and pin.isdigit()):
    print("Lock Opened!")
else:
    print("Error Wrong Pin , Please Enter 4 Digit Pin!")