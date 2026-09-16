n= int(input())
org = n
sum = 0
divisor = 1

while divisor<n:
    if n%divisor==0:
        sum+=divisor
    divisor+=1

if sum==org and org>1:
    print("Perfect Number")
else:
    print("Not Perfect Number")