id = int(input('qual a sua idade?'))

if id == 18:
    print('voce tem que se alistar')
elif id < 18 :
    print('voce ainda vai se alistar, faltam {} anos'.format(18 - id))
elif id > 18 :
    print('ja passou o tempo do seu alistamento, voce esta pendente a {} anos'.format(id - 18 ))
