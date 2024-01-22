vl = float(input('qual a velocidade atual do carro:'))
mu = float((vl - 80) * 7.0)
if vl <= 80 :
    print('cuidado voce quase esta sendo multado:')
else:
    print('voce foi multado em {:.2f}, pois voce esta {}Km/h a cima do limite de 80Km/h'.format(mu, vl - 80))
