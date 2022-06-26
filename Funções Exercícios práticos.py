def ent( ):
    spam = [[2, 4, 6, 8, 10],['a', 'b', 'c', 'd'],'hello']
    return spam


saida = ent()

for line in saida:
    print(line,'=', len(line))

print(saida)