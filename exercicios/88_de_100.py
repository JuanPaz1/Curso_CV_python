import random
import time

njogos = int(input('Quantos jogos você quer fazer? '))
jogos = []

while njogos > 0:
    nnum = 6
    numjogos = []

    while nnum > 0:
        num = random.randint(0, 60)

        # Verifica se o número já está no jogo atual
        while num in numjogos:
            num = random.randint(0, 60)

        numjogos.append(num)
        nnum -= 1
        numjogos.sort()
    # Adiciona o jogo atual à lista de jogos
    jogos.append(numjogos)
    njogos -= 1

# Imprime todos os jogos gerados
for jogo in jogos:
    print(jogo)
    time.sleep(0.5)