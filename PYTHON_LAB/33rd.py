bill = int(input())

if(bill>5000):
    print("Discount: " , bill*20/100)
    print("Final  Amount:", bill - bill*20/100)

elif(3000<bill<=5000):
    print("Discount: " , bill*10/100)
    print("Final  Amount:", bill - bill*10/100)

elif(bill<3000):
    print("No Discount , Final Bill:" , bill)