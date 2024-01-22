frase=str(input('diga uma frase')).strip().upper()
palavras = frase.split()
junto = ' '.join(palavras)
inverso = ' '.join(palavras)
print('voce digitou a frase {}'.format(frase))
for letras in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('temos um palindromo')
else:
    print('não é palindromo')
print(junto , inverso)