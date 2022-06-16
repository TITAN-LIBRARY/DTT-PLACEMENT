'''
declare a dict
a: apple, b:banana, c:cat, d:dog

I/P: abc
Expected O/P: apple banana cat

I/P: a
Expected O/P: apple
'''

dict = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cat',
    'd': 'dog'
}

s = input("Enter the value: ")

for i in s:
    print(dict.get(i, "Not Found"), end=' ')
