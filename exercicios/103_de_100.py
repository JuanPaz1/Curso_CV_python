def ficha(a='desconhecido', b=0):
    x = a
    y = b
    return x, y

print(20 * '=-=')
a = str(input('Qual é o nome do jogador? '))
b = int(input('Quantos gols ele fez? '))

nome, gols = ficha(a, b)

print(f'\nO jogador {nome} fez {gols} gols.')
