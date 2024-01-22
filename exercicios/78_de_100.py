valores = list()
for v in range (0 , 5):
    valores.append(int(input('digite um valor:')))

locmax = valores.index(max(valores))
locmin = valores.index(min(valores))

print('o maior valor é {} é o menor é {} nas pósições {} e {}'.format(max(valores), min(valores), locmax , locmin))
