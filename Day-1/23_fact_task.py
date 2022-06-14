'''
Odd means print cube root
even means fact
'''


def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)


n = int(input("Enter the number: "))

if n % 2 == 0:
    print(fact(n))
else:
    print(n**3)
