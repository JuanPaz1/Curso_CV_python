dias = float(input('quantos dias voce vai alugar?'))
km = float(input('quantos km voce rodou com o carro?'))

cdias = dias*60
ckm = km*0.15

print('como você usou o carro por {:.0f} e percorreu {} km, voce deve pagar R${}'.format(dias,km, cdias+ckm))
