num = int(input())

is_neg = num < 0
num = abs(num)

rev_num = 0
while num > 0 :
    last = num%10
    rev_num = (rev_num*10)+ last
    num = num//10

if is_neg:
    rev_num = -rev_num

print(f"Reversed Number: {rev_num}")