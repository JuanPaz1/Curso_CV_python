valores = list()
valorespares = list()
valoresimpar = list()
rev = 0
while True:
    valores.insert(0, int(input('digite um valor [digite algo menos que zero para parar]:')))
    rev = valores[0]
    if rev % 2 == 0:
        valorespares.insert(0, rev)
        if valorespares[0] < 0:
            valorespares.pop(0)
    else:
        valoresimpar.insert(0,rev)
        if valoresimpar[0] < 0:
            valoresimpar.pop(0)
    if rev < 0:
        valores.pop(0)
        break
valores.sort()
valoresimpar.sort()
valorespares.sort()
print('Segue as seguintes listagems: \nLista original: {} \nLista de Valores Pares: {} \nLista de Valores Impares: {}'.format(valores, valorespares, valoresimpar))