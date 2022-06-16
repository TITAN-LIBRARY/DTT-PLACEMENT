heros = ['iron man', 'doctor strange', 'hulk']

vow = "aeiou"
l = []

for i in heros:
    stwr = ""
    for j in i:
        if j not in vow:
            stwr = stwr + j
    l.append(stwr)

print(l)

print(l[::-1])
