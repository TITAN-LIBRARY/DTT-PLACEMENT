# Check given number is perfect or not.
# Perfect Num means sum of all thier factors is equal to that number.

import math

n = int(input("Enter the num: "))
sum = 0

'''
TC = O(n)
q = n//2+1

for i in range(1, q):
    if n % i == 0:
        sum += i
if sum == n:
    print("YES")
else:
    print("NO")
'''

q = math.floor(math.sqrt(n))

for i in range(2, q+1):
    if n % i == 0:
        sum = sum + i + n//i


if sum == n:
    print("YES")
else:
    print("NO")
