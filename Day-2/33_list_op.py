'''
heros = ["iron man", "spiderman", "black panter", "hulk"]
exp output:

["iron man", "doctor strange", "hulk"]

'''


heros = ["iron man", "spiderman", "black panter", "hulk"]

# heros = str(heros)
# heros.insert(1, 'doctor strange')
# heros.remove('black panter', 'spiderman')

heros[1:3] = ["doctor strange"]


print(heros)
