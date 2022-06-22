# Find the sum of individual digits of 'n' repeated 'r' times.

n = int(input("Enter the num: "))
r = int(input("Enter the r: "))

sum = 0

if n % 9 == 0:
    sum = 9
else:
    sum = n % 9

if (r*sum) % 9 == 0:
    sum = 9
else:
    sum = (r*sum) % 9

print("Sum is: ", sum)
