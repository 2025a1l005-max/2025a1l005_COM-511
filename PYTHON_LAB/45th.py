'''
wap to repeatedly calculate the sum of digits of a nu. until the result becomes a single digit.
'''
n = int(input("Enter a number: "))

while n > 9:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    n = total

print("Single digit result:", n)