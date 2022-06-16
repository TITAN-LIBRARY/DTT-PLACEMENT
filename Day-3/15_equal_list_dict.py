

dict = {}
key = list(map(int, input().strip().split()))
value = list(map(int, input().strip().split()))

if len(key) != len(value):
    print("Not equal")
else:
    for i in range(len(key)):
        for j in range(len(value)):
            if i == j:
                dict[key[i]] = value[j]
    print(dict)
