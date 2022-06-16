# In two line
l = list(map(int, input("Enter elements: ").split()))
print(list(set(l)))

# In One line

print(list(set(list(map(int, input("Enter elements: ").split())))))
