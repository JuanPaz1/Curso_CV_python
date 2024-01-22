itens = ( 'lapis', 1.75,
          'borracha', 2,
          'caderno', 5,
          'estojo', 15.90,
          'compaso', 9.99,
          'livro', 34.90)
for item in range(0, len(itens)):
    if item % 2 ==0:
        print(itens[item], end=' ')
    else:
        print(itens[item])