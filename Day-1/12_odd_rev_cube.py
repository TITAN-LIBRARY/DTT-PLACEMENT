'''
take int as input
if it is odd print reverse + 23
if even print it's cube root
'''


def rev_num(n):
    dig = 0
    m = n
    while(m != 0):
        r = m % 10
        dig = dig*10 + r
        m = m//10
    return(dig+23)


n = int(input("Enter the Number: "))

if n % 2 == 0:
    print(n**(1/3))
else:
    print(rev_num(n))
