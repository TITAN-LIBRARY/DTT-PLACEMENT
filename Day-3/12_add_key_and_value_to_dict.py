'''
I/P:

Key: 1,2,3
value: 1,2,3

O/P:
{1:1, 2:2, 3:3}
'''

'''
l=[['a',1], ['b',2]]
l[i[j]] = k
l[i[j+1]] = v
'''

d = {}
u = int(input("Enter the number of elements: "))
for i in range(u):
    k = input("Key: ")
    v = input("Value: ")
    d[k] = v
print(d)

# l = list(list(list(map(str, input("Enter the key value pair sep by coma: ").split(' ')))))


# print(l)
