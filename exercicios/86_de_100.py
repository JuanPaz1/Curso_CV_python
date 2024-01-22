matrix = list()
for c in range(0 , 3):
    linha = list()
    for l in range(0 , 3):
        valor = (int(input('Selecione o valor para [{} , {}]:'.format(c, l))))
        linha.insert(l, valor)
    matrix.append(linha)
print('{} \n{}\n{}'.format(matrix[0:-2],matrix[1:-1],matrix[2:]))
