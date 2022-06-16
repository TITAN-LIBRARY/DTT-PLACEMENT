import math

from numpy import mat


l = list(map(int, input("Enter the elements: ").split()))
s = []
ns = []
for i in l:
    x = int(math.sqrt(i))
    if x**2 == i:
        print("Is a perfect Square: ", math.factorial(i))
