import random
lista = list()
for j in range (0, 4):
    jogadores = dict()
    jogadores['jogador'] = str(input('nome:'))
    vdado = random.randint(1 , 20)
    jogadores['valor do dado'] = vdado
    lista.append(jogadores)
lista.sort(key =lambda x: x['valor do dado'], reverse=True)
for v in lista:
    print(v)
