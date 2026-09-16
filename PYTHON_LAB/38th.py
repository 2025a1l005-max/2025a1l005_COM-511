usr = "Arjun"
psw = "12345678"

usr1 = input()
psw1 = input()

if(usr==usr1 and psw==psw1):
    print("Login Successful")
else:
    print("Try Again: ")
    usr2 = input() 
    psw2 = input()
    if(usr==usr2 and psw==psw2):
        print("Login Successful")
    else:
        print("Try Again: ")
        usr3 = input() 
        psw3 = input()
        if(usr==usr3 and psw==psw3):
            print("Login Successful")
        else:
            print("Account Locked!")
