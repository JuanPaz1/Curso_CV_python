lista = []

while True:
    jogadores = dict()
    jogadores['NOME JOGADOR'] = str(input('Qual o nome do jogador?'))
    jogadores['JOGOS JOGADOS'] = int(input('Quantos jogos ele jogou?'))

    for jogo in range(jogadores['JOGOS JOGADOS']):
        gols = int(input('Quantos gols foram marcados na partida {}?'.format(jogo + 1)))
        lista.append(gols)
        jogadores['TOTAL'] = jogadores.get('TOTAL', 0) + gols

    vld = str(input('Deseja continuar? [S/N]')).upper()
    if vld == 'N':
        break

    for chave, valor in jogadores.items():
        print('O campo {} tem valor {}'.format(chave, valor))

    print('O jogador {} jogou {} partidas'.format(jogadores['NOME JOGADOR'], jogadores['JOGOS JOGADOS']))

for partida, gols in enumerate(lista, start=1):
    print('Na partida {}, fez {} gols'.format(partida, gols))
