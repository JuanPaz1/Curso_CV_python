lista = list()
for n in range (0, 3):
    alunos = dict()
    alunos['nome'] = str(input('Qual o nome do aluno?'))
    alunos['media'] = float(input('qual foi sua media?'))
    if alunos['media'] >= 7:
        alunos['Situação'] = 'APROVADO'
    else:
        alunos['Situação'] = 'REPROVADO'
    lista.append(alunos.copy())
for aluno in lista:
    print(aluno)

