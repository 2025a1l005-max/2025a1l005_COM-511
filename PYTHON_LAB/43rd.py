num = int(input("Enter number: "))
st=""
if(num==0):print("0")
while num>0:
    bit=num%2
    st=str(bit)+st
    num//=2

print(st) 