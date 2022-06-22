# Find the sum of individual digits of number 'n' upto single digit.

n = int(input("Enter the num: "))

sum = 0

if n % 9 == 0:
    sum = 9
else:
    sum = n % 9

print("Sum is: ", sum)
