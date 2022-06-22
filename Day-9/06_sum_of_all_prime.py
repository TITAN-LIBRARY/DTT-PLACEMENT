# Sum of all Prime between 1 billion.
# Use Sieve of Eratosthenes algorithm
# TC O(n)+O(root(n)log(n))


import math


n = int(input("Enter the num: "))

l = [1]*(n+1)

q = math.floor(math.sqrt(n)) + 1

for i in range(2, q):
    if l[i] == 1:
        for j in range(i*i, n+1, i):
            l[j] = 0

sum = 0
for i in range(2, n+1):
    if l[i] == 1:
        sum += i

print(sum)
