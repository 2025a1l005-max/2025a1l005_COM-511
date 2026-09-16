# Loop through numbers from 1 to 50
for number in range(1, 51):
    if number % 4 == 0:
        continue  
    print(number, end=' ')