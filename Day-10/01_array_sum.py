n = int(input("Enter the num: "))
psa = []
a = []

psa[0] = a[0]

for i in range(1, n):
    psa[i] = psa[i-1] + a[i]

q = int(input("Enter the number of times: "))

for i in range(1, q+1):
    l = int(input("Enter up limit: "))
    r = int(input("Enter lower limit: "))

    if l == 0:
        sum = psa[1]
    sum = psa[1] - psa[l-1]

print(sum)
