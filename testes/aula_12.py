nome = str(input('qual o seu nome?'))
if nome == 'Juan':
    print('que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('seu nome é bem popular no brasil {}'.format(nome))
else:
    print('seu nome é comum {}'.format(nome))
print('tenha um bom dia {}'.format(nome))