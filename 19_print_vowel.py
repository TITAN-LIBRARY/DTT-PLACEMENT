n = input("Enter the string: ")

a = "aeiou"

fin = ""

for i in n:
    if i in a:
        fin += i

print(fin)
