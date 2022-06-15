
a = list(map(int, input("Enter the numbers: ").split(' ')))
m = 1
s = 0
for i in range(len(a)):
    if i % 2 == 0:
        m = m * a[i]
    else:
        s = s + a[i]

print("Product :", m)
print("Sum :", s)
