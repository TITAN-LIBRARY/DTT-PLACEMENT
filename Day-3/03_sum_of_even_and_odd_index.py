'''
even: 2+4+6
odd: 1+3+5
print mod value of even-odd
'''

import math

l = list(map(int, input("Enter the list elements: ").split()))
odd = 0
even = 0

'''
for i in range(len(l)):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i
print("Absolute value: ", abs(even-odd))
'''


# Alternate

print("Absolute value: ", abs(sum(l[0::2])-sum(l[1::2])))
