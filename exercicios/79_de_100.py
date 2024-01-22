valores = list()
rev = 0
while True:
    valores.insert(0 ,int(input('digite um valor [digite algo menos que zero para parar]:')))
    rev = valores[0]
    if rev < 0:
        valores.pop(0)
        break
    if rev in valores[1:]:
        valores.remove(rev)
valores.sort()
print('aqui esta a sua lista de numeros:\n {}'.format(valores))
