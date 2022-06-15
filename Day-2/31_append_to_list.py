
'''
take a num as I/P
if odd append fact(num) else append num ** 4
'''


def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fact(n-1)


a = []
n = int(input("ENter the no of number: "))

for i in range(0, n):
    x = int(input("ENter the number: "))
    if x % 2 == 0:
        a.append(x**4)
    else:
        a.append(fact(x))

print(a)
