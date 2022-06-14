
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)


n = int(input("Enter the number: "))

a = 1
if n == 1 or n == 0:
    print(1)
for i in range(1, n+1):
    a = a*i
    # print(i)

print(a)

print(fact(n))
