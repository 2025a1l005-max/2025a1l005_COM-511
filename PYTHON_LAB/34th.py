pas = input()

while len(pas)<8 or '@' not in pas:
    print("Weak Password. Try Again!")
    pas = input()  
print("Password Accepted")
