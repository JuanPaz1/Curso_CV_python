lista = []
totp = 0
totidi = 0
listaf = []
listamed = []

while True:
    pessoas = dict()
    pessoas['NOME'] = str(input('Qual o seu nome?')).upper()
    pessoas['SEXO'] = str(input('Qual o seu sexo? [M/F]')).upper()
    pessoas['IDADE'] = int(input('Qual a sua idade?'))
    lista.append(pessoas.copy())
    totp += 1

    if pessoas['SEXO'] == 'F':
        listaf.append(pessoas.copy())

    vld = str(input('Deseja continuar? [S/N]')).upper()
    if vld != 'S':
        break

for pessoa in lista:
    totidi += pessoa['IDADE']

media = totidi / totp

for pessoa in lista:
    if pessoa['IDADE'] > media:
        listamed.append(pessoa.copy())

print('Ao todo foram cadastradas {} pessoas'.format(totp))
print('A média de idade do grupo é {:.2f}'.format(media))
print('Todas as mulheres cadastradas são: \n{}'.format(listaf))
print('Pessoas com idade acima da média: \n{}'.format(listamed))
