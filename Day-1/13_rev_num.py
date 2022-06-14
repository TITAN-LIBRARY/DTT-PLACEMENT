
m = int(input("Enter the Number: "))
dig = 0

while(m != 0):
    r = m % 10
    dig = dig*10 + r
    m = m//10

print(dig)

# alternate in single line
print(input("Enter the number ")[::-1])

# here :: means slicing from the last
