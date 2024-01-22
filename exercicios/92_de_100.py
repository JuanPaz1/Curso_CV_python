import datetime

lista = []
ano_atual = datetime.date.today().year

while True:
    pessoa = dict()
    pessoa['NOME'] = str(input('Qual o nome?'))
    pessoa['NASCIMENTO'] = int(input('Em qual ano você nasceu?'))
    pessoa['IDADE'] = ano_atual - pessoa['NASCIMENTO']
    pessoa['PIS'] = int(input('Qual o número do PIS? [0 caso não tenha]'))

    if pessoa['PIS'] != 0:
        pessoa['ANO CONTRATACAO'] = int(input('Qual o ano da sua contratação?'))
        pessoa['SALARIO'] = float(input('Qual era o salário?'))
        pessoa['TEMPO DE TRABALHO'] = ano_atual - pessoa['ANO CONTRATACAO']
        pessoa['APOSENTADORIA'] = (35 - pessoa['TEMPO DE TRABALHO'])

    lista.append(pessoa)

    stop = str(input('Deseja continuar? [S/N]')).upper()
    if stop != 'S':
        break

for pessoa in lista:
    print('{}, com {} anos, vai se aposentar daqui a {} anos'.format(pessoa['NOME'], pessoa['IDADE'], pessoa.get('APOSENTADORIA', 0)))
