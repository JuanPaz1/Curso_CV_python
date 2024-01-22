import datetime


def voto(nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - nascimento

    if idade < 16:
        resultado = 'NEGADO'
    elif 16 <= idade < 18 or idade >= 70:
        resultado = 'OPCIONAL'
    else:
        resultado = 'OBRIGATORIO'

    return resultado


print(20 * '=')
print('VOTAÇÃO')
nascimento = int(input('Qual é o ano do seu nascimento? '))

resultado = voto(nascimento)
print(f'Sua situação de voto é: {resultado}')

