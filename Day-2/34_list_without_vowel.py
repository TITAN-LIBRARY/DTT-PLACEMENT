
heros = ['iron man', 'doctor strange', 'hulk']

a = "aeiou"


for i in range(len(heros)):
    for vowel in a:
        heros[i] = heros[i].replace(vowel, "")

print(heros)
