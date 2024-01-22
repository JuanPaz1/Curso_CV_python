valores = list()
for c in range(0 , 5):
    valores.append(int(input('digite um valor:')))
for c, v in enumerate (valores):
    print('na posição {} encontrei valor {}'.format(c , v))
print('cheguei ao final da lista')