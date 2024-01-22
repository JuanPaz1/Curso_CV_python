galera = list()
dados = list()
totmai = totmen = 0
for c in range (0 , 3):
    dados.append(str(input('Qual o Seu Nome:')))
    dados.append(int(input('qual a sua idade:')))
    galera.append(dados[:])
    dados.clear

for p in galera:
    if p[1] >= 21:
        print('{} é maior de idade'.format(p[0]))
        totmai +=1
    else:
        print('{} é menor de idade'.format(p[0]))
        totmen +=1
print('temos o total de {} mariores e {} de menores'.format(totmai, totmen))
