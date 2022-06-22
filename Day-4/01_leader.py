n = int(input("Enter the elements no."))
l = []

for i in range(0, n):
    x = int(input("Ebter the elemets: "))
    l.append(x)
max = l[0]

# print()
for i in range(0, n):
    if l[i+1] > max:
        max = l[i+1]
        print(l[i], end=' ')

print(l[n-1])
