

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)


d = {}
l1 = []
l2 = []

u = int(input("Enter the number of elements: "))
for i in range(u):
    k = int(input("Key: "))
    v = int(input("Value: "))
    d[k] = v

    if k % 7 == 0:
        l1.append(v**3)
    else:
        l2.append(fact(v))

print("List Div of 7: ", l1)
print("Fact of value", l2)
print("Sum: ", sum(l1)+sum(l2))
print(d)
