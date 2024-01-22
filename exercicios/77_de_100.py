palavras = ('aprender', 'programar', 'linguagem')

for p in palavras:
    print('\nna palavra {} temos'.format(p) , end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')