n = input("Enter the string: ")

a = "aeiou"

for i in range(0, len(n)):
    if n[i] in a:
        print(i)

# with find()

for i in n:
    if i in a:
        x = n.find(i)
        print(x)

        for i in n[2::]:
            if i in a:
                print(n.find(i))

print()
