name = ('Ricardo', 1, 2, 3, 'Paulo', 'cat', 'dog', 5)

tro = []

for line in name:
    print(line, '=', type(line))
    if not type(line) == str:
        tro.append(str(line))
print(tro)
for line in tro:
    if not type(line)==str:
        print('Errado!')
    else:
        print(line,'Certo!', type(line))
print(type(tro))

print('')

name = ['Ricardo', 1, 2, 3,  5]
name02 = ['Paulo', 'cat', 'dog']
print(name)
print(name02)
name = name02
print(name)
print(name02)