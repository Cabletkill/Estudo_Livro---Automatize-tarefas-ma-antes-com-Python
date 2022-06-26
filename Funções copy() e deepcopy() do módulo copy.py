import copy

name = ['Ricardo de Souza Silva', "Ricardina"]
nome02 = [1, 2,[2, 4, 6, 8, 10],['a', 'b', 'c', 'd'],'hello', 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


namecopy = copy.deepcopy(nome02)
namecopy[2] = name
del name[1]
print(namecopy)
print(name)
print(nome02)


