lista = list()

while True:
    alunos = list()  # Criando uma nova lista para cada aluno
    nomealu = str(input('Digite qual o nome do aluno:'))
    n1 = float(input('Digite a primeira nota:'))
    n2 = float(input('Digite a segunda nota:'))
    m = (n1 + n2) / 2

    lista.append([nomealu, [n1, n2], m])

    conf = str(input('Deseja continuar? [S/N]:')).upper()

    if conf != 'S':
        break

print('-=' * 20)
print('{:<3} | {:<12} | {:>8}'.format("No.", "NOME", "MÉDIA"))

for c, aluno in enumerate(lista):
    print('{:<3} | {:<12} | {:>8.2f}'.format(c, aluno[0], aluno[2]))
while True:
    opc = int(input('mostar a nota de qual aluno? [999 para]'))
    if opc == 999:
        print('final')
        break
    if opc <= len(lista) - 1:
        print('notas de {} são {}'.format(lista[opc][0], lista[opc][1]))
