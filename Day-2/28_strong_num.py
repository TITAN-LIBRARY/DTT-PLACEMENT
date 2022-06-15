import math

n = int(input("Enter the num: "))

m = n
sum = 0

while m != 0:
    r = m % 10
    m = m//10
    c = math.factorial(r)
    sum = sum + c

if sum == n:
    print("Yes")
else:
    print("No")
