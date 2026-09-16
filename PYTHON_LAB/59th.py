# Write a menu-driven Python program where the user can add items, remove items, view cart, and exit.


cart = []
while True:
    c = input("\n1.Add 2.Remove 3.View 4.Exit: ")
    if c=="1": cart.append(input("Item: "))
    elif c=="2":
        i=input("Item: ")
        if i in cart: cart.remove(i)
    elif c=="3": print("Cart:",cart)
    elif c=="4": break
