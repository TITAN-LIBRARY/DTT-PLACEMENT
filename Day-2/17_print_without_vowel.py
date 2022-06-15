n = input("Enter the string: ")

a = "aeiou"

# for i in n:
#     if i not in a:
#         print(i, end="")

# alternate
fin = ""
for i in n:
    if i not in a:
        fin += i

print(fin)
