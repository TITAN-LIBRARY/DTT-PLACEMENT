'''
Take int as input
print it's reverse added with 23
'''


n = int(input("Enter the number: "))
dig = 0
m = n
while (m != 0):
    r = m % 10
    dig = dig*10 + r
    m = m//10


print(dig+23)
