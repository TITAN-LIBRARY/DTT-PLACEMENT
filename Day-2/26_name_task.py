# take name as input if len > 8 print (Hi + name) \n nice to meet you else print Hello + name \n pleased to meet you.


name = input("Enter the name: ")

l = len(name)

if l > 8:
    print(f"Hi {name} \nNice to meet you..!")
    # print("Nice to meet you..!")
else:
    print(f"Hello {name} \nPleased to meet you..!")
    # print("Pleased to meet you..!")
