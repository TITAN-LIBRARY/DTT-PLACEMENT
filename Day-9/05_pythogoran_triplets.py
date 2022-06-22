# Find pythogoran triplet below 'n'.

# Eg: (3,4,5), (5,12,1), (6,8,10), (9,12,15), (12, 16, 20)

n = int(input("Enter the num: "))

a = b = c = 0

m = 2
count = 0

while c <= n:
    for i in range(1, m):
        # a = m*m = i*i
        a = m*m
        b = 2*m*i
        c = m*m + i*i
        if c <= n:
            count += 1
    m += 1

print(count)
