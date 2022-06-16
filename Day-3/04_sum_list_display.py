'''
input: 1 2 3 4 5

Expected Output: [1, 3, 6, 10, 15]
'''

l = list(map(int, input("Enter the number").split()))

l1 = []

sum = l[0]
l1.append(sum)
for i in range(1, len(l)):
    sum = sum + l[i]

    l1.append(sum)

print(l1)
