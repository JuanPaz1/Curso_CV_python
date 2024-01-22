frase = str(input('digite uma frase: ')).lower().strip()

c = frase.count('a')
lf = frase.rfind('a') +1
f = frase.find('a')+1


print('na sua frase tem {} letras "a" a primeira na posição {} e a ultima na posição {}'.format(c, f , lf))

