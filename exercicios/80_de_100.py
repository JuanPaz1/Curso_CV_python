valores = list()
for v in range(0,5):
    var = int(input('Digite um valor:'))
    valores.insert(var,var)

print('Os valores digitados em ordem foram {}'.format(valores))