n = []
for c in range(0, 4):
    valor = int(input(f'Digite um valor:'))
    n.append(valor)
print('valores digitados:', n)
print(n.count(9))
print(n.index(3)+1)
print(sum(1 for valor in n if valor % 2 == 0))
