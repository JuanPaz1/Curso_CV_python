pessoas = list()
dados = list()
minpeso = maxpeso = 0
totpessoas=0

while True:
    dados.append(str(input('Digite um nome:')))
    dados.append(float(input('Digite seu peso:')))

    if len(dados) == 0:
        maxpeso = minpeso = dados[1]
    else:
        if dados[1] > maxpeso:
            maxpeso = dados[1]
        if dados[1] < minpeso:
            minpeso = dados[1]
    pessoas.append(dados[:])

    dados.clear()

    totpessoas +=1



    ver = input('Deseja continuar?[S/N]').upper()
    if ver != 'S':
        break
print('foram cadastrados {} pessoas \nOs pessos minimos foram {:.2f} \nOS pessos maximos foram {:.2f}'.format(totpessoas, maxpeso, minpeso))
for p in pessoas:
    if p[1] == maxpeso:
        print('{}'.format(p[0]))


for p in pessoas:
    if p[1] == minpeso:
        print('{}'.format(p[0]))
