'''s = "sriram"
print(s.replace('r', 'o'))'''

name = list(input("Enter the name: ").split(' '))
a = "aeiou"
for i in range(len(name)):
    for vowel in a:
        name[i] = name[i].replace(vowel, "")

fname, lname = str(name)
