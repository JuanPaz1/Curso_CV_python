valores = list()
rev = 0
count = 0
while True:
    valores.insert(0 ,int(input('digite um valor [digite algo menos que zero para parar]:')))
    rev = valores[0]
    count+=1
    if rev < 0:
        valores.pop(0)
        if 5 in valores:
            rev5 = 'o valor 5 foi digitado'
        else:
            rev5 = 'o valor 5 nao foi digitado'
        break
valores.sort(reverse=True)
print('Sua lista de numero: {}\nTotal de numeros digitados: {}\ne {}'.format(valores, count, rev5))