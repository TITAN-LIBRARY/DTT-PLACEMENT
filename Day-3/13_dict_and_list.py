'''
I/P: 

Key: 1
Value: 7
Key: 2
Value: 5
Key: 3
Value: 14

O/P:
List Div of 7:  [343, 2744]
Fact of value [120]
Sum:  3207
{1: 7, 2: 5, 3: 14}

'''

import math

d = {}
l1 = []
l2 = []

u = int(input("Enter the number of elements: "))
for i in range(u):
    k = int(input("Key: "))
    v = int(input("Value: "))
    d[k] = v

    if v % 7 == 0:
        l1.append(v**3)
    else:
        l2.append(math.factorial(v))

print("List Div of 7: ", l1)
print("Fact of value", l2)
print("Sum: ", sum(l1)+sum(l2))
print(d)
