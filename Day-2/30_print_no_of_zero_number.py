
'''
given a num, if strong num print yes else find number of 0's
'''

import math

n = list(input("Enter the number: "))

m = str(n)

sum = 0

for i in n:
    sum = sum + math.factorial(int(i))

count = str(sum).count('0')
print("No of 0's is: ", count)
