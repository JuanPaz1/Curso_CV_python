maior = 0
for c in range (1,7 + 1):
    an = int(input('qual o seu ano de nascimento?'))
    m = 2023 - an
    if m >= 21 :
        maior = maior + 1
print(' ao todo {} são maiores de idade'.format(maior))

