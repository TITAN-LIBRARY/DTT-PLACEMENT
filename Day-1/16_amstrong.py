
n = input("Enter the number: ")

l = len(n)

n = int(n)

sum = 0

m = n
dig = 0
while(m != 0):
    r = m % 10
    dig = r
    m = m//10

    sum = sum + dig**l


if (n == sum):
    print("It is Armstrong..")
else:
    print("Not an Amstrong..")
