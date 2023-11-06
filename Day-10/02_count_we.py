

s = input("Enter the string: ")

l = len(s)

e = [0]*l

pse = []

for i in range(l):
    if s[i] == 'e':
        e[i] = 1

pse[l-1] = e[l-1]

for i in range(l-2, 0, -1):
    pse[i] = pse[i+1] + e[i]

ans = 0

for i in range(l):
    if s[i] == 'w':
        ans += pse[i]

print(ans)
