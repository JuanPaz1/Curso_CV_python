import random
print('escolha')
jokenpo = int(input(' 1 - para PEDRA \n 2 - para TESOURA \n 3 - PAPEL \nEscolha:'))

adv = random.randint(1 , 3)

if jokenpo == 1 and adv == 1 or jokenpo == 2 and adv == 2 or jokenpo == 3 and adv == 3:
    print('empate {} , {}'.format(jokenpo,adv))
elif jokenpo == 1 and adv == 2 or jokenpo == 2 and adv == 3 or jokenpo == 3 and adv == 1:
    print('voce ganhou {} , {}'.format(jokenpo,adv))
elif jokenpo == 1 and adv == 3 or jokenpo == 2 and adv == 1 or jokenpo == 3 and adv == 2:
    print('perdeu {} , {}'.format(jokenpo,adv))
else:
    print('tente de novo')

