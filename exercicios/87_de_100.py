matrix = list()
vpar=0
for c in range(0 , 3):
    linha = list()
    for l in range(0 , 3):
        valor = (int(input('Selecione o valor para [{} , {}]:'.format(c, l))))
        if valor%2 ==0:
            vpar+=valor
        linha.insert(l, valor)
    matrix.append(linha)

somac3 = 0
for linha in matrix:
    somac3 += linha[2]

print('{} \n{}\n{}'.format(matrix[0:-2],matrix[1:-1],matrix[2:]))
print('a soma de todos os valores pares é {}'.format(vpar))
print('a soma de todos os numeros da terceira coluna é {}'.format(somac3))
print('o maior valor da linha 2 é {}'.format(max(matrix[1])))