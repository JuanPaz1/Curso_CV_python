n1 = float(input('qual a distancia da sua viagem?')).__trunc__()

if n1 <= 200:
    print('o preço da sua passagem é: {}'.format(n1*0.50))
else:
    print('o preço da sua passagem é: {}'.format(n1*0.45))
