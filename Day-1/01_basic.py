a = 12  # int

b = 11.12  # float

c = 'a'  # string/char

d = "Hi"  # string

# To print statements like 'I like "Python".' To make these things possible python has this feature.

e = True  # boolean

# print(type(c))

# Concatenation can only strings with strings

print("Print I like {} and {}".format("Python", "C++"))

# alternate
a = 'I like "Python"'
print(f'{a} with IDE')
# the curly braces interacts with the variables present in the program

print("{} with IDE".format(23+23))

# without using format() or format string
a = 23
print(a+23, " with IDs")
